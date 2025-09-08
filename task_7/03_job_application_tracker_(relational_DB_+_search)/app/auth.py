from fastapi import Depends, HTTPException, Header
from sqlmodel import Session, select
from .database import get_session
from .models import User

def get_current_user(
    username: str = Header(..., alias="X-User"),
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or missing user")
    return user
