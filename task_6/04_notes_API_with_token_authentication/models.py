from pydantic import BaseModel
from datetime import date

class Note(BaseModel):
    title: str
    content: str
    date: date
