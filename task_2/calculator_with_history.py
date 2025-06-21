# Task 3: Calculator with History

# Scenario: A basic calculator that remembers past results.

# Instructions:

# - Show options: Add, Subtract, Multiply, Divide, View History, Exit

# - Use input to take two numbers and perform operation

# - Store each operation and result in a list

# - Show history with index numbers

# - Use functions for operations and error handling for divide-by-zero
    

history = []

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error (divide by zero)"
    return a / b

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. View History\n6. Exit")
    choice = input("Choose: ")

    if choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == "1":
                result = add(a, b)
                history.append(f"{a} + {b} = {result}")
            elif choice == "2":
                result = subtract(a, b)
                history.append(f"{a} - {b} = {result}")
            elif choice == "3":
                result = multiply(a, b)
                history.append(f"{a} * {b} = {result}")
            elif choice == "4":
                result = divide(a, b)
                history.append(f"{a} / {b} = {result}")
            print("Result:", result, "\n")
        except ValueError:
            print("Invalid number input.\n")

    elif choice == "5":
        for i, record in enumerate(history):
            print(f"{i + 1}. {record}")
        print()
    elif choice == "6":
        break
    else:
        print("Invalid option.\n")
