from pydantic import BaseModel
from datetime import date

class JobApplication(BaseModel):
    job_title: str
    company: str
    date_applied: date
    status: str   # e.g., "pending", "interview", "rejected", "accepted"
