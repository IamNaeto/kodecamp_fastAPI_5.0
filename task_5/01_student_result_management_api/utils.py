import json
from typing import List
from models import Student

FILE_PATH = "students.json"

def calculate_average(scores: dict) -> float:
    return sum(scores.values()) / len(scores)

def assign_grade(avg: float) -> str:
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def load_students() -> List[Student]:
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return [Student(**student) for student in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_students(students: List[Student]):
    with open(FILE_PATH, "w") as f:
        json.dump([s.dict() for s in students], f, indent=4)
