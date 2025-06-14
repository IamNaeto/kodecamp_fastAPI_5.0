# Task 5: Simple ATM Simulator
# Scenario: Simulate a basic ATM system that allows a user to perform multiple banking operations.

# Instructions:

# - Start with a fixed account balance (e.g., $1,000).

# - Show a menu in a loop:

#      1. Check Balance

#      2. Deposit

#      3. Withdraw

#      4. Exit

# - For each choice:

#      - If 1: Show current balance.

#      - If 2: Ask how much to deposit, add to balance (ensure amount is positive).

#      -  If 3: Ask how much to withdraw.

#            - If amount > balance, show error.

#            - Else, subtract from balance.

#      - If 4: Exit the loop.

# - After exit, display a goodbye message with the final balance.

balance = 1000.0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")
    print()

    if choice == "1":
        print("Current balance: $", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        print()
        if amount > 0:
            balance += amount
            print("Deposited:", amount)
            print("New balance: $", balance)
        else:
            print("Invalid deposit amount.")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        print()
        if amount > balance:
            print("Insufficient funds.")
        elif amount > 0:
            balance -= amount
            print("Withdrawn:", amount)
            print("New balance: $", balance)
        else:
            print("Invalid withdrawal amount.")
    elif choice == "4":
        print("Goodbye! Final balance is $", balance)
        break
    else:
        print("Invalid option.")


