from __future__ import annotations
import json
import os
from typing import Optional, Dict
from passlib.context import CryptContext

USERS_FILE = os.getenv("USERS_FILE", os.path.join(os.path.dirname(__file__), "users.json"))
_pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def load_users() -> Dict:
    if not os.path.exists(USERS_FILE):
        default_hash = _pwd_ctx.hash("admin")
        data = {"users": [{"username": "admin", "password_hash": default_hash}]}
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return data
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(data: Dict) -> None:
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_user_by_username(username: str) -> Optional[Dict]:
    data = load_users()
    for u in data.get("users", []):
        if u.get("username") == username:
            return u
    return None


def add_user(username: str, password: str) -> Dict:
    data = load_users()
    if get_user_by_username(username):
        raise ValueError("User already exists")
    data.setdefault("users", []).append({"username": username, "password_hash": _pwd_ctx.hash(password)})
    save_users(data)
    return {"username": username}


def verify_password(plain: str, hashed: str) -> bool:
    return _pwd_ctx.verify(plain, hashed)
