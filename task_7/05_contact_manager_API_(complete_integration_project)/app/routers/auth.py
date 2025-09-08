from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm

from .. import models, schemas, auth
from ..database import get_session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=schemas.UserRead)
def signup(user_in: schemas.UserCreate, session: Session = Depends(get_session)):
    existing = session.exec(select(models.User).where((models.User.username == user_in.username) | (models.User.email == user_in.email))).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    user = models.User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=auth.get_password_hash(user_in.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.post("/token", response_model=schemas.Token)
def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = auth.authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
