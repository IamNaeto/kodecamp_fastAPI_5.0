from __future__ import annotations
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

# --- Auth ---

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    username: str
    password: str

class SignupRequest(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class UserRead(BaseModel):
    id: int
    username: str
    is_admin: bool

# --- Product ---

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = Field(ge=0)

class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    stock: int

# --- Cart ---

class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)

class CartItemRead(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    line_total: float

class CartSummary(BaseModel):
    items: List[CartItemRead]
    subtotal: float

# --- Orders ---

class OrderItemRead(BaseModel):
    product_id: int
    quantity: int
    price_each: float
    line_total: float

class OrderRead(BaseModel):
    id: int
    total: float
    created_at: datetime
    items: List[OrderItemRead]
