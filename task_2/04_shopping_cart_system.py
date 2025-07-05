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


print("\nAvailable Items:\n- Rice: $400\n- Beans: $350\n- Oil: $500")
items = {"rice": 400, "beans": 350, "oil": 500}
cart = []

def add_cart():
    name = input("Enter item name: ").lower()
    if name in items:
        try:
            qty = int(input("Enter quantity: "))
            cart.append({"item": name, "quantity": qty, "price": items[name]})
            print(f"Added {qty} x {name.title()} to cart.\n")
        except:
            print("Invalid quantity.\n")
    else:
        print("Item not available.\n")

def view_cart():
    total = 0
    print("--- Cart ---")
    for c in cart:
        subtotal = c['quantity'] * c['price']
        total += subtotal
        print(f"{c['item'].title()} x{c['quantity']} - ${subtotal}")
    print("Total:", f"${total}\n")

def checkout():
    total = sum(c['quantity'] * c['price'] for c in cart)
    print("Checkout complete.\nYou paid:", f"${total}\nThank you for shopping!\n")
    cart.clear()

def remove():
    name = input("Enter item to remove: ").lower()
    for c in cart:
        if c['item'] == name:
            cart.remove(c)
            print("Item removed.\n")
            return
    print("Item not found.\n")

def clear():
    cart.clear()
    print("Cart cleared.\n")

while True:
    print("1. Add to Cart\n2. View Cart\n3. Checkout\n4. Remove Item\n5. Clear Cart\n6. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1": add_cart()
    elif choice == "2": view_cart()
    elif choice == "3": checkout()
    elif choice == "4": remove()
    elif choice == "5": clear()
    elif choice == "6": break
    else: print("Invalid choice.\n")