import json
import os

def load_entries(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_entries(filename, entries):
    with open(filename, 'w') as f:
        json.dump(entries, f, indent=4)
