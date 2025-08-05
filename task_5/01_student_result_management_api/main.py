from fastapi import FastAPI, HTTPException
from models import Student
from utils import calculate_average, assign_grade, load_students, save_students

app = FastAPI()

@app.post("/students/", response_model=Student)
def add_student(student: Student):
    try:
        students = load_students()
        if any(s.name.lower() == student.name.lower() for s in students):
            raise HTTPException(status_code=400, detail="Student already exists.")
        
        student.average = calculate_average(student.subject_scores)
        student.grade = assign_grade(student.average)
        students.append(student)
        save_students(students)
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/{name}", response_model=Student)
def get_student(name: str):
    try:
        students = load_students()
        for student in students:
            if student.name.lower() == name.lower():
                return student
        raise HTTPException(status_code=404, detail="Student not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/", response_model=list[Student])
def list_students():
    try:
        return load_students()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
