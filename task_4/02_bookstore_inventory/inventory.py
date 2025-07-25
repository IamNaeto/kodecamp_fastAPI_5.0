import json
import os
import math
from book import Book

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "books.json")

def load_inventory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            books_data = json.load(f)
            return [Book.from_dict(b) for b in books_data]
    return []

def save_inventory(books):
    with open(DATA_FILE, 'w') as f:
        json.dump([b.to_dict() for b in books], f, indent=4)

def add_book(inventory):
    title = input("Title: ")
    author = input("Author: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Invalid input. Try again.")
        return
    book = Book(title, author, price, stock)
    inventory.append(book)
    print(f"Book '{title}' added.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    for book in inventory:
        print(f"{book.title} by {book.author} | ${book.price:.2f} | Stock: {book.stock}")

def search_books(inventory, keyword):
    results = [b for b in inventory if keyword.lower() in b.title.lower()]
    return results
