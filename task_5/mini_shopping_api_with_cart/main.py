from fastapi import FastAPI, HTTPException
from cart import load_products, add_to_cart, checkout
from models import Product, CartItem

app = FastAPI()

@app.get("/products/", response_model=list[Product])
def get_products():
    return load_products()

@app.post("/cart/add", response_model=list[CartItem])
def add_item_to_cart(product_id: int, qty: int):
    try:
        return add_to_cart(product_id, qty)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/cart/checkout")
def checkout_cart():
    return checkout()
