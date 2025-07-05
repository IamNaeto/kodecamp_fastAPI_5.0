import json
import os

def load_books(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_books(filename, books):
    with open(filename, 'w') as f:
        json.dump(books, f, indent=4)
