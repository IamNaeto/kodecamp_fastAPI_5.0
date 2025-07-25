import os
import json
from datetime import datetime
from transaction import Transaction
from budget_utils import group_by_category, calculate_totals

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "transactions.json")

def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Transaction.from_dict(d) for d in data]
    return []

def save_transactions(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in transactions], f, indent=4)

def add_transaction(transactions):
    date_str = input("Enter date (YYYY-MM-DD) or press ENTER for today: ")
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g. Food, Rent, Transport): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    t = Transaction(date_str, category, amount)
    transactions.append(t)
    print("Transaction added.")

def view_summary(transactions):
    totals = calculate_totals(transactions)
    if not totals:
        print("No transactions to summarize.")
        return
    print("\n=== Expense Summary ===")
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")

def main():
    transactions = load_transactions()
    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add transaction")
        print("2. View summary")
        print("3. Save and Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_summary(transactions)
        elif choice == '3':
            save_transactions(transactions)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
