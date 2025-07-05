# Task 3: Calculator with History

# Scenario: A basic calculator that remembers past results.

# Instructions:

# - Show options: Add, Subtract, Multiply, Divide, View History, Exit

# - Use input to take two numbers and perform operation

# - Store each operation and result in a list

# - Show history with index numbers

# - Use functions for operations and error handling for divide-by-zero
    

print("\nSimple Calculator")
history = []

def calc(op):
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if op == "1":
            res = a + b
            history.append(f"{a} + {b} = {res}")
        elif op == "2":
            res = a - b
            history.append(f"{a} - {b} = {res}")
        elif op == "3":
            res = a * b
            history.append(f"{a} * {b} = {res}")
        elif op == "4":
            if b == 0:
                print("Error: Cannot divide by zero.\n")
                return
            res = a / b
            history.append(f"{a} / {b} = {res}")
        print("Result:", res, "\n")
    except:
        print("Invalid input.\n")

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. View History\n6. Exit")
    choice = input("\nEnter your choice: ")
    if choice in ["1","2","3","4"]: calc(choice)
    elif choice == "5":
        print("--- Calculation History ---")
        for i, h in enumerate(history):
            print(f"{i+1}. {h}")
        print()
    elif choice == "6": break
    else: print("Invalid choice.\n")