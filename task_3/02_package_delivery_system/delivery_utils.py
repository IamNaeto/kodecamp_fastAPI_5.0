import json
import os

def load_packages(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_packages(filename, packages):
    with open(filename, 'w') as f:
        json.dump(packages, f, indent=4)
