# Task 2: Fast Food Order System
# Scenario: A fast-food ordering system that supports multiple customers.

# Instructions:

# - Use a loop to serve multiple customers (stop when user types 'exit').

# - For each customer:

#      - Ask for name and quantity of:

#      - Burger ($5), Fries ($2), Drink ($1.5)

#      - Calculate total.

#      - If total > $20, apply 10% discount.

#      - Display the bill.

# - After exit, show how many customers were served

# customers = 0

while True:
    name = input("\nEnter customer name (or type 'exit' to finish): ")
    if name == "exit":
        break

    burgers = int(input("Enter quantity of Burgers ($5): "))
    fries = int(input("Enter quantity of Fries ($2): "))
    drinks = int(input("Enter quantity of Drinks ($1.5): "))

    total = burgers * 5 + fries * 2 + drinks * 1.5

    if total > 20:
        discount = total * 0.10
        total -= discount
        print(f"Discount of ${discount:.2f} applied.")

    print(f"{name}'s total bill: ${total:.2f}")
    customers += 1

print("\nTotal customers served:", customers)