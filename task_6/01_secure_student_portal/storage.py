import json, os
from fastapi import HTTPException, status
from typing import Dict

STUDENTS_FILE = os.environ.get("STUDENTS_FILE", "students.json")

def load_students() -> Dict[str, dict]:
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)
        return {}
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="students.json is corrupted or unreadable."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to read students.json."
        )

def save_students(data: Dict[str, dict]) -> None:
    try:
        with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to write students.json."
        )
