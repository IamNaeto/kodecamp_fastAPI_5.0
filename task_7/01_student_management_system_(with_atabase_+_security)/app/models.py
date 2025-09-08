from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from datetime import datetime

class Grade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    course: str
    score: int
    student_id: Optional[int] = Field(default=None, foreign_key="student.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    student: Mapped["Student"] = Relationship(back_populates="grades")


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str

    grades: Mapped[List[Grade]] = Relationship(back_populates="student")
