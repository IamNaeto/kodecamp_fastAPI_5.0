from __future__ import annotations
import json
from pathlib import Path
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..database import get_session
from ..models import CartItem, Product, Order, OrderItem
from ..schemas import AddToCartRequest, CartItemRead, CartSummary, OrderRead, OrderItemRead
from ..security import get_current_user

ORDERS_JSON = Path(__file__).resolve().parents[1] / "orders.json"

router = APIRouter(prefix="/cart", tags=["cart"])

def get_cart_summary(user_id: int, session: Session) -> CartSummary:
    q = select(CartItem, Product).where(CartItem.user_id == user_id).where(CartItem.product_id == Product.id)
    rows = session.exec(q).all()
    items: List[CartItemRead] = []
    subtotal = 0.0
    for cart_item, product in rows:
        line = product.price * cart_item.quantity
        subtotal += line
        items.append(CartItemRead(
            product_id=product.id, name=product.name, price=product.price,
            quantity=cart_item.quantity, line_total=line
        ))
    return CartSummary(items=items, subtotal=subtotal)

@router.post("/add/", response_model=CartSummary, status_code=201)
def add_to_cart(payload: AddToCartRequest, session: Session = Depends(get_session), user=Depends(get_current_user)):
    product = session.get(Product, payload.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if payload.quantity > product.stock:
        raise HTTPException(status_code=400, detail="Not enough stock")

    existing = session.exec(
        select(CartItem).where(CartItem.user_id == user.id, CartItem.product_id == product.id)
    ).first()

    if existing:
        new_qty = existing.quantity + payload.quantity
        if new_qty > product.stock:
            raise HTTPException(status_code=400, detail="Not enough stock")
        existing.quantity = new_qty
        session.add(existing)
    else:
        session.add(CartItem(user_id=user.id, product_id=product.id, quantity=payload.quantity))

    session.commit()
    return get_cart_summary(user.id, session)

@router.get("/", response_model=CartSummary)
def view_cart(session: Session = Depends(get_session), user=Depends(get_current_user)):
    return get_cart_summary(user.id, session)

@router.post("/checkout/", response_model=OrderRead)
def checkout(session: Session = Depends(get_session), user=Depends(get_current_user)):
    # Load cart
    cart_rows = session.exec(
        select(CartItem, Product).where(CartItem.user_id == user.id).where(CartItem.product_id == Product.id)
    ).all()

    if not cart_rows:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Verify stock again and compute totals
    total = 0.0
    for cart_item, product in cart_rows:
        if cart_item.quantity > product.stock:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for {product.name}")
        total += product.price * cart_item.quantity

    # Create order
    order = Order(user_id=user.id, total=total)
    session.add(order)
    session.commit()
    session.refresh(order)

    # Create order items, decrease stock, clear cart
    items_read: List[OrderItemRead] = []
    for cart_item, product in cart_rows:
        session.add(OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=cart_item.quantity,
            price_each=product.price
        ))
        # stock decrement
        product.stock -= cart_item.quantity
        session.add(product)

        items_read.append(OrderItemRead(
            product_id=product.id,
            quantity=cart_item.quantity,
            price_each=product.price,
            line_total=product.price * cart_item.quantity
        ))

        session.delete(cart_item)

    session.commit()
    session.refresh(order)

    # Backup order to orders.json
    try:
        ORDERS_JSON.touch(exist_ok=True)
        with ORDERS_JSON.open("r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
            data.append({
                "order_id": order.id,
                "user_id": user.id,
                "total": order.total,
                "created_at": order.created_at.isoformat(),
                "items": [
                    {"product_id": i.product_id, "quantity": i.quantity, "price_each": i.price_each}
                    for i in session.exec(select(OrderItem).where(OrderItem.order_id == order.id)).all()
                ]
            })
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=2)
    except Exception:
        # Don't block checkout if backup fails
        pass

    return OrderRead(id=order.id, total=order.total, created_at=order.created_at, items=items_read)
