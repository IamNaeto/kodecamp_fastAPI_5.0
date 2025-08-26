from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import json, os
from models import Product, CartItem
from auth import authenticate_user, create_access_token, admin_required, customer_required

app = FastAPI()

PRODUCTS_FILE = "products.json"
CART_FILE = "cart.json"

# Ensure files exist
if not os.path.exists(PRODUCTS_FILE):
    with open(PRODUCTS_FILE, "w") as f: json.dump([], f)

if not os.path.exists(CART_FILE):
    with open(CART_FILE, "w") as f: json.dump([], f)


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/admin/add_product/")
def add_product(product: Product, user=Depends(admin_required)):
    with open(PRODUCTS_FILE, "r+") as f:
        products = json.load(f)
        products.append(product.dict())
        f.seek(0)
        json.dump(products, f, indent=2)
    return {"msg": "Product added", "product": product}


@app.get("/products/")
def get_products():
    with open(PRODUCTS_FILE, "r") as f:
        return json.load(f)


@app.post("/cart/add/")
def add_to_cart(cart_item: CartItem, user=Depends(customer_required)):
    with open(CART_FILE, "r+") as f:
        cart = json.load(f)
        cart.append(cart_item.dict())
        f.seek(0)
        json.dump(cart, f, indent=2)
    return {"msg": "Added to cart", "cart_item": cart_item}
