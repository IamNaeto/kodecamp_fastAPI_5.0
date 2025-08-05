import json
import math
from typing import List
from models import Product, CartItem

CART_FILE = "cart.json"
PRODUCTS_FILE = "products.json"

def load_products() -> List[Product]:
    try:
        with open(PRODUCTS_FILE, "r") as f:
            data = json.load(f)
            return [Product(**item) for item in data]
    except FileNotFoundError:
        return []

def load_cart() -> List[CartItem]:
    try:
        with open(CART_FILE, "r") as f:
            data = json.load(f)
            return [CartItem(**item) for item in data]
    except FileNotFoundError:
        return []

def save_cart(cart: List[CartItem]):
    with open(CART_FILE, "w") as f:
        json.dump([item.dict() for item in cart], f, indent=4)

def add_to_cart(product_id: int, qty: int):
    products = load_products()
    product = next((p for p in products if p.id == product_id), None)

    if not product:
        raise ValueError("Product not found")

    cart = load_cart()
    existing_item = next((item for item in cart if item.product_id == product_id), None)

    total_price = round(product.price * qty, 2)

    if existing_item:
        existing_item.quantity += qty
        existing_item.total_price = round(existing_item.quantity * product.price, 2)
    else:
        cart.append(CartItem(
            product_id=product.id,
            name=product.name,
            price=product.price,
            quantity=qty,
            total_price=total_price
        ))

    save_cart(cart)
    return cart

def checkout():
    cart = load_cart()
    total = sum(item.total_price for item in cart)
    rounded_total = math.ceil(total)
    return {
        "items": cart,
        "total": total,
        "rounded_total": rounded_total
    }
