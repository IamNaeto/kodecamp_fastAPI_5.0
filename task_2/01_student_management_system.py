# Task 1: Student Management System

# Goal: Build a program to store student names and their scores using lists/dictionaries.

# Core Features:

# - Add new students (with 3 subject scores)

# - Show all students with average and performance status

# - Search for a student by name

# - Use functions for actions

# - Use error handling for invalid inputs


students = []

def add_student():
    name = input("Enter student name: ")
    try:
        scores = []
        for i in range(1, 4):
            score = float(input(f"Enter score {i}: "))
            scores.append(score)
        students.append({"name": name, "scores": scores})
        print("Student added successfully.\n")
    except ValueError:
        print("Invalid score input. Please enter numbers.\n")

def show_all_students():
    if not students:
        print("No students to show.\n")
        return

    for student in students:
        avg = sum(student["scores"]) / 3
        if avg < 50:
            status = "Fail"
        elif avg < 80:
            status = "Pass"
        else:
            status = "Excellent"
        print(f"{student['name']} - Avg: {avg:.2f} - Status: {status}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:", student)
            found = True
            break
    if not found:
        print("Student not found.\n")

while True:
    print("1. Add Student\n2. Show All\n3. Search Student\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid option.\n")
