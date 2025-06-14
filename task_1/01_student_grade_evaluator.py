# Task 1: Student Grade Evaluator
# Scenario: Collect and evaluate grades for multiple students

# Instructions:

# - Ask how many students to process.

# - Use a loop to:

#      - Ask for each student's name and 3 subject scores.

#      - Convert scores to float, calculate the average.

#      - Display result:

#      - Average < 50 -> Fail

#      - 50-79 -> Pass

#      - 80+ -> Excellent!

# - After all students are processed, display a summary:

#  how many passed, failed, and got excellent

passed = 0
failed = 0
excellent = 0

students = int(input("How many students to process? "))

for i in range(students):
    name = input("\nEnter student name: ")
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))

    average = (score1 + score2 + score3) / 3
    print(f"{name}'s average is: {average:.2f}")

    if average < 50:
        print("Result: Fail")
        failed += 1
    elif average < 80:
        print("Result: Pass")
        passed += 1
    else:
        print("Result: Excellent!")
        excellent += 1

print("\nSummary:")
print("Passed:", passed)
print("Failed:", failed)
print("Excellent:", excellent)