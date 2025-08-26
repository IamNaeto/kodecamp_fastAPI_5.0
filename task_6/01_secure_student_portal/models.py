from pydantic import BaseModel, Field
from typing import List

class StudentRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=128)
    grades: List[float] = Field(default_factory=list, description="List of numeric grades")

class StudentPublic(BaseModel):
    username: str
    grades: List[float] = []

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
