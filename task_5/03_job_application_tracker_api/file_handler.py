import json
from typing import List
from models import JobApplication

FILE_PATH = "applications.json"

def load_applications() -> List[JobApplication]:
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return [JobApplication(**app) for app in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_applications(applications: List[JobApplication]):
    with open(FILE_PATH, "w") as f:
        json.dump([app.dict() for app in applications], f, indent=4)
