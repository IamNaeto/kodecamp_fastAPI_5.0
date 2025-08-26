from fastapi import APIRouter, Depends, HTTPException
from models import StudentPublic
from storage import load_students
from security import get_current_username

router = APIRouter(prefix="", tags=["grades"])

@router.get("/grades/", response_model=StudentPublic)
async def get_grades(username: str = Depends(get_current_username)):
    students = load_students()
    user = students.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return StudentPublic(username=username, grades=user.get("grades", []))
