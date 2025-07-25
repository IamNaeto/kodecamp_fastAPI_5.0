from inventory import (
    load_inventory,
    save_inventory,
    add_book,
    view_inventory,
    search_books 
)

def main():
    inventory = load_inventory()

    while True:
        print("\n=== Bookstore Inventory ===")
        print("1. Add book")
        print("2. View inventory")
        print("3. Search books")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            results = search_books(inventory, keyword)
            if results:
                for book in results:
                    print(f"{book.title} by {book.author} | ${book.price:.2f} | Stock: {book.stock}")
            else:
                print("No matching books found.")
        elif choice == '4':
            save_inventory(inventory)
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice.")
