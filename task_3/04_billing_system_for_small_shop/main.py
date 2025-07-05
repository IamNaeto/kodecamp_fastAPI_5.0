from billing import Cart

# --- Main Menu ---
cart = Cart()

while True:
    print("---------------------------------------------")
    print("         Billing System for Small Shop       ")
    print("---------------------------------------------")
    print("         Welcome to the Billing System!      ")
    print("                Choose an option:            ")
    print("---------------------------------------------")
    print("         1. Add Product to Cart              ")
    print("         2. View Cart and Total              ")
    print("         3. Checkout and Save Bill           ")
    print("         4. View Previous Transactions       ")
    print("         5. Exit                             ")
    print("---------------------------------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Product name: ")
        try:
            price = float(input("Price (₦): "))
            quantity = int(input("Quantity: "))
            cart.add_product(name, price, quantity)
        except ValueError:
            print("Invalid price or quantity.\n")
    elif choice == "2":
        cart.view_cart()
    elif choice == "3":
        cart.checkout()
    elif choice == "4":
        cart.view_history()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number.\n")
