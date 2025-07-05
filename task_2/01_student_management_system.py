# Task 1: Student Management System

# Goal: Build a program to store student names and their scores using lists/dictionaries.

# Core Features:

# - Add new students (with 3 subject scores)

# - Show all students with average and performance status

# - Search for a student by name

# - Use functions for actions

# - Use error handling for invalid inputs


students = []

print("Welcome to the Student Management System")

def add_student():
    name = input("Enter student name: ")
    try:
        math = float(input("Enter score for Math: "))
        eng = float(input("Enter score for English: "))
        sci = float(input("Enter score for Science: "))
        students.append({"name": name, "scores": [math, eng, sci]})
        print(f"Student '{name}' added successfully!\n")
    except ValueError:
        print("Invalid score input.\n")

def view_all():
    if not students:
        print("No students found.\n")
        return
    print("--- Student Records ---")
    for s in students:
        avg = sum(s['scores']) / 3
        status = "Fail" if avg < 50 else "Pass" if avg < 80 else "Excellent"
        print(f"Name: {s['name']}\nScores: {s['scores']}\nAverage: {avg}\nStatus: {status}\n")

def search():
    name = input("Enter name to search: ")
    for s in students:
        if s['name'].lower() == name.lower():
            avg = sum(s['scores']) / 3
            status = "Fail" if avg < 50 else "Pass" if avg < 80 else "Excellent"
            print("Student found!")
            print(f"Scores: {s['scores']}\nAverage: {avg}\nStatus: {status}\n")
            return
    print("Student not found.\n")

while True:
    print("1. Add New Student\n2. View All Students\n3. Search Student by Name\n4. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1": add_student()
    elif choice == "2": view_all()
    elif choice == "3": search()
    elif choice == "4": break
    else: print("Invalid choice.\n")