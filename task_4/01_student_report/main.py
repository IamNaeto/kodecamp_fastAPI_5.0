# main.py

import json
import os
from student import Student

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'students.json')

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Student.from_dict(d) for d in data]
    return []

def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump([s.to_dict() for s in students], f, indent=4)

def add_student(students):
    name = input("Enter student name: ")
    subjects_scores = {}
    while True:
        subject = input("Enter subject (or press ENTER to stop): ")
        if subject == "":
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            subjects_scores[subject] = score
        except ValueError:
            print("Invalid score. Try again.")
    new_student = Student(name, subjects_scores)
    students.append(new_student)
    print(f"Student '{name}' added successfully.")

def view_students(students):
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"\nName: {s.name}")
        for subj, score in s.subjects_scores.items():
            print(f"  {subj}: {score}")
        print(f"  Average: {s.average:.2f}")
        print(f"  Grade: {s.grade}")

def update_student(students):
    name = input("Enter the name of the student to update: ")
    for s in students:
        if s.name.lower() == name.lower():
            print("Enter new scores for subjects:")
            for subj in s.subjects_scores:
                try:
                    new_score = float(input(f"{subj} (current: {s.subjects_scores[subj]}): "))
                    s.subjects_scores[subj] = new_score
                except ValueError:
                    print("Invalid input. Skipping.")
            s.average = s.calculate_average()
            s.grade = s.calculate_grade()
            print(f"{s.name}'s record updated.")
            return
    print("Student not found.")

def main():
    students = load_students()
    while True:
        print("\n=== Student Report Card App ===")
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Save and exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            save_students(students)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
