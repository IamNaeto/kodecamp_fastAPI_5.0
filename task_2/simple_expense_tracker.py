# Task 2: Simple Expense Tracker

# Scenario: Help users track their daily expenses.

# Instructions:

# - Let user enter multiple expenses: description + amount

# - Store as a list of dictionaries e.g., {"item": "Transport", "amount": 150.0}

# - Allow menu options:

#  - Add expense

#  - View all expenses

#  - Total and average

#  - Exit

# - Use try-except for amount input

# - Use loops and functions


expenses = []

def add_expense():
    item = input("Enter expense description: ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"item": item, "amount": amount})
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    for exp in expenses:
        print(f"{exp['item']}: ${exp['amount']:.2f}")
    print()

def show_summary():
    if not expenses:
        print("No expenses to summarize.\n")
        return
    total = sum(e["amount"] for e in expenses)
    avg = total / len(expenses)
    print(f"Total: ${total:.2f}, Average: ${avg:.2f}\n")

while True:
    print("1. Add Expense\n2. View Expenses\n3. Total & Average\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice.\n")
