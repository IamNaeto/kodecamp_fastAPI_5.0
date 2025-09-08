from __future__ import annotations
from fastapi import APIRouter, HTTPException
from datetime import timedelta
from ..schemas import Token, LoginRequest
from ..security import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=Token)
def login(payload: LoginRequest):
    user = authenticate_user(payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": user["username"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register", status_code=201)
def register(payload: LoginRequest):
    from ..utils import add_user

    try:
        user = add_user(payload.username, payload.password)
        return {"message": "User created", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
