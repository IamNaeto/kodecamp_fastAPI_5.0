from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
import secrets
from models import StudentRegister, StudentPublic, TokenResponse
from storage import load_students, save_students
from security import hash_password, verify_password, TOKENS

router = APIRouter(prefix="", tags=["auth"])

@router.post("/register/", response_model=StudentPublic, status_code=201)
def register(student: StudentRegister):
    students = load_students()
    if student.username in students:
        raise HTTPException(status_code=400, detail="Username already exists.")
    students[student.username] = {"password_hash": hash_password(student.password), "grades": student.grades}
    save_students(students)
    return StudentPublic(username=student.username, grades=student.grades)

@router.post("/login/", response_model=TokenResponse)
def login(form: OAuth2PasswordRequestForm = Depends()):
    students = load_students()
    user = students.get(form.username)
    if not user or not verify_password(form.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password.")
    token = secrets.token_urlsafe(32)
    TOKENS[token] = form.username
    return TokenResponse(access_token=token)
