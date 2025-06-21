# Task 4: Shopping Cart System

# Scenario: Simulate a mini-store system.

# Instructions:

# - Show a list of available items with prices (use a dictionary)

# - Let the user "add to cart" by entering item name and quantity

# - Store cart in a list of dictionaries:

#  {"item": "Rice", "quantity": 2, "price": 400}

# - Calculate total bill

# - Option to remove an item or clear cart

# - Loop until user exits

# - Handle invalid inputs and missing items


items = {
    "rice": 400,
    "beans": 300,
    "oil": 250,
    "milk": 150
}
cart = []

def show_items():
    print("Available items:")
    for item, price in items.items():
        print(f"{item.title()} - ${price}")
    print()

def add_to_cart():
    item = input("Enter item to add: ").lower()
    if item in items:
        try:
            qty = int(input("Enter quantity: "))
            cart.append({"item": item, "quantity": qty, "price": items[item]})
            print("Added to cart.\n")
        except ValueError:
            print("Invalid quantity.\n")
    else:
        print("Item not available.\n")

def remove_item():
    item = input("Enter item to remove: ").lower()
    for c in cart:
        if c["item"] == item:
            cart.remove(c)
            print("Removed from cart.\n")
            return
    print("Item not found in cart.\n")

def clear_cart():
    cart.clear()
    print("Cart cleared.\n")

def view_cart():
    if not cart:
        print("Cart is empty.\n")
        return
    total = 0
    for c in cart:
        subtotal = c["quantity"] * c["price"]
        total += subtotal
        print(f"{c['item'].title()} x {c['quantity']} = ${subtotal}")
    print("Total Bill:", f"${total:.2f}\n")

while True:
    print("1. Show Items\n2. Add to Cart\n3. View Cart\n4. Remove Item\n5. Clear Cart\n6. Exit")
    choice = input("Choose: ")
    if choice == "1":
        show_items()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        clear_cart()
    elif choice == "6":
        break
    else:
        print("Invalid choice.\n")
