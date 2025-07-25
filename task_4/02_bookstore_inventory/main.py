from inventory import load_inventory, save_inventory, add_book, view_inventory

def main():
    inventory = load_inventory()

    while True:
        print("\n=== Bookstore Inventory ===")
        print("1. Add book")
        print("2. View inventory")
        print("3. Save and Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_book(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            save_inventory(inventory)
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
