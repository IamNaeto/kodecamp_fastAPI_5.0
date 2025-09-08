from __future__ import annotations
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from ..database import get_session
from ..models import Student, Grade
from ..schemas import StudentCreate, StudentRead, StudentUpdate, GradeCreate, GradeRead
from ..security import get_current_user
from fastapi import status

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=StudentRead, status_code=201)
def create_student(payload: StudentCreate, session: Session = Depends(get_session)):
    # Check for existing email
    existing = session.exec(select(Student).where(Student.email == payload.email)).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A student with this email already exists."
        )

    # Create ORM object
    student = Student(name=payload.name, age=payload.age, email=payload.email)
    session.add(student)
    session.commit()
    session.refresh(student)
    return StudentRead(
        id=student.id,
        name=student.name,
        age=student.age,
        email=student.email,
        grades=[]
    )


@router.get("/", response_model=List[StudentRead])
def list_students(session: Session = Depends(get_session), skip: int = Query(0), limit: int = Query(50),
                  q: Optional[str] = Query(None)):
    stmt = select(Student)
    if q:
        q_like = f"%{q}%"
        stmt = stmt.where((Student.name.ilike(q_like)) | (Student.email.ilike(q_like)))
    stmt = stmt.offset(skip).limit(limit)
    students = session.exec(stmt).all()

    results = []
    for s in students:
        grades = session.exec(select(Grade).where(Grade.student_id == s.id)).all()
        results.append(StudentRead(
            id=s.id, name=s.name, age=s.age, email=s.email,
            grades=[GradeRead(id=g.id, course=g.course, score=g.score, created_at=g.created_at) for g in grades]
        ))
    return results


@router.get("/{student_id}", response_model=StudentRead)
def get_student(student_id: int, session: Session = Depends(get_session)):
    s = session.get(Student, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    grades = session.exec(select(Grade).where(Grade.student_id == s.id)).all()
    return StudentRead(
        id=s.id, name=s.name, age=s.age, email=s.email,
        grades=[GradeRead(id=g.id, course=g.course, score=g.score, created_at=g.created_at) for g in grades]
    )


@router.patch("/{student_id}", response_model=StudentRead)
def update_student(student_id: int, payload: StudentUpdate, session: Session = Depends(get_session), user=Depends(get_current_user)):
    s = session.get(Student, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    if payload.name is not None:
        s.name = payload.name
    if payload.age is not None:
        s.age = payload.age
    if payload.email is not None:
        s.email = payload.email
    session.add(s)
    session.commit()
    session.refresh(s)

    grades = session.exec(select(Grade).where(Grade.student_id == s.id)).all()
    return StudentRead(
        id=s.id, name=s.name, age=s.age, email=s.email,
        grades=[GradeRead(id=g.id, course=g.course, score=g.score, created_at=g.created_at) for g in grades]
    )


@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, session: Session = Depends(get_session), user=Depends(get_current_user)):
    s = session.get(Student, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(s)
    session.commit()
    return {"message": f"Student with id {student_id} deleted successfully"}


@router.post("/{student_id}/grades", response_model=GradeRead, status_code=201)
def add_grade(student_id: int, payload: GradeCreate, session: Session = Depends(get_session), user=Depends(get_current_user)):
    s = session.get(Student, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    g = Grade(course=payload.course, score=payload.score, student_id=student_id)
    session.add(g)
    session.commit()
    session.refresh(g)
    return GradeRead(id=g.id, course=g.course, score=g.score, created_at=g.created_at)


@router.get("/{student_id}/grades", response_model=List[GradeRead])
def list_grades(student_id: int, session: Session = Depends(get_session)):
    s = session.get(Student, student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    grades = session.exec(select(Grade).where(Grade.student_id == student_id)).all()
    return [GradeRead(id=g.id, course=g.course, score=g.score, created_at=g.created_at) for g in grades]
