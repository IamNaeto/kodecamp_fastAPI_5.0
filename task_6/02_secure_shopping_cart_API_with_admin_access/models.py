from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    role: str  # "admin" or "customer"

class Product(BaseModel):
    id: int
    name: str
    price: float

class CartItem(BaseModel):
    username: str
    product_id: int
    quantity: int
