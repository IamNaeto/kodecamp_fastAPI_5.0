from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from .database import engine
from .routers import auth as auth_router, contacts as contacts_router
from . import models

app = FastAPI(title="Contact Manager API")

# Create DB tables
SQLModel.metadata.create_all(engine)

# Allow CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware to log IP address of every request
@app.middleware("http")
async def log_client_ip(request: Request, call_next):
    client_host = request.client.host if request.client else "unknown"
    path = request.url.path
    method = request.method
    print(f"Request from IP: {client_host} -> {method} {path}")
    response = await call_next(request)
    # Optionally add header
    response.headers["X-Client-IP"] = client_host
    return response

# Routers
app.include_router(auth_router.router)
app.include_router(contacts_router.router)

# basic root
@app.get("/")
def root():
    return {"message": "Contact Manager API"}
