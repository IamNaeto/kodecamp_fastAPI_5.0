from __future__ import annotations
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .middleware import ResponseTimeMiddleware
from .routers import users, products, cart

ALLOWED_ORIGINS = ["http://localhost:3000"]

app = FastAPI(title="E-Commerce API", version="1.0.0")

app.add_middleware(ResponseTimeMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/", tags=["health"])
def health():
    return {"message": "E-Commerce API is running"}
