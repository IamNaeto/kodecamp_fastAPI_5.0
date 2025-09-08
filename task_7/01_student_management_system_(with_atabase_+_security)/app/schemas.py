from __future__ import annotations
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel


class GradeRead(SQLModel):
    id: int
    course: str
    score: float
    created_at: datetime


class GradeCreate(SQLModel):
    course: str
    score: float


class StudentCreate(SQLModel):
    name: str
    age: int
    email: str
    grades: Optional[List[GradeCreate]] = None


class StudentRead(SQLModel):
    id: int
    name: str
    age: int
    email: str
    grades: List[GradeRead] = []


class StudentUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(SQLModel):
    username: str
    password: str
