import json
import os

def load_employees(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_employees(filename, employees):
    with open(filename, 'w') as f:
        json.dump(employees, f, indent=4)
