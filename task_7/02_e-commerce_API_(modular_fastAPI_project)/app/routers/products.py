from __future__ import annotations
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..database import get_session
from ..models import Product
from ..schemas import ProductCreate, ProductRead
from ..security import require_admin

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/admin/products/", response_model=ProductRead, status_code=201)
def create_product(payload: ProductCreate, session: Session = Depends(get_session), admin=Depends(require_admin)):
    product = Product(name=payload.name, price=payload.price, stock=payload.stock)
    session.add(product)
    session.commit()
    session.refresh(product)
    return ProductRead(id=product.id, name=product.name, price=product.price, stock=product.stock)

@router.get("/", response_model=List[ProductRead])
def list_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return [ProductRead(id=p.id, name=p.name, price=p.price, stock=p.stock) for p in products]
