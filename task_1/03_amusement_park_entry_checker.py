# Task 3: Amusement Park Entry Checker
# Scenario: Check multiple visitors' ticket prices.

# Instructions:

# - Use a loop to allow repeated entries.

# - For each visitor:

#      - Ask name and age (int).

#      - Based on age:

#      - < 5: Free

#      - 5-17: $5

#      - 18-59: $10

#      - 60+: $7

#      - Ask if they have a coupon (Yes/No). If yes, apply 20% discount.

#      - Show final price.

# - Exit loop when a special name like 'done' is entered.

while True:
    name = input("\nEnter visitor name (or 'done' to exit): ")
    if name == "done":
        break

    age = int(input("Enter age: "))

    if age < 5:
        price = 0
    elif age <= 17:
        price = 5
    elif age <= 59:
        price = 10
    else:
        price = 7

    coupon = input("Do you have a coupon? (Yes/No): ")
    if coupon.lower() == "yes":
        price = price * 0.20

    print("Final ticket price:", f"${price:.2f}")