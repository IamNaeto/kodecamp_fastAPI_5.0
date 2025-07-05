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
print("\nWelcome to Expense Tracker")

def add_exp():
    desc = input("Enter item description: ")
    try:
        amt = float(input("Enter amount: "))
        expenses.append({"item": desc, "amount": amt})
        print("Expense added successfully.\n")
    except:
        print("Invalid amount.\n")

def view_all_exp():
    print("--- All Expenses ---")
    for i, e in enumerate(expenses):
        print(f"{i+1}. {e['item']} - ${e['amount']:.2f}")
    print()

def total_avg():
    total = sum(e['amount'] for e in expenses)
    avg = total / len(expenses) if expenses else 0
    print(f"Total Expenses: ${total:.2f}\nAverage Expense: ${avg:.2f}\n")

while True:
    print("1. Add Expense\n2. View All Expenses\n3. View Total and Average\n4. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1": add_exp()
    elif choice == "2": view_all_exp()
    elif choice == "3": total_avg()
    elif choice == "4": break
    else: print("Invalid choice.\n")