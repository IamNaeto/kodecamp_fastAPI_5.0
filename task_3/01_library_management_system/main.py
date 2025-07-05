from library_utils import load_books, save_books

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["available"])

import os
from library_utils import load_books, save_books

class Library:
    def __init__(self, filename="books.json"):
        current_dir = os.path.dirname(__file__)
        self.filename = os.path.join(current_dir, filename)
        self.books = [Book.from_dict(b) for b in load_books(self.filename)]


    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' by {author} added.\n")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'.\n")
                else:
                    print("Book is currently not available.\n")
                return
        print("Book not found.\n")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"You have returned '{book.title}'.\n")
                else:
                    print("This book was not borrowed.\n")
                return
        print("Book not found.\n")

    def view_books(self):
        if not self.books:
            print("No books in the library.\n")
            return
        print("--- Library Collection ---")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"'{book.title}' by {book.author} - {status}")
        print()

    def save_and_exit(self):
        save_books(self.filename, [b.to_dict() for b in self.books])
        print("Library saved. Goodbye!")

# --- Main Menu ---
library = Library()

while True:
    print("------------------------------------------------------------")
    print("                 Library Management System                  ")
    print("------------------------------------------------------------")
    print("         Welcome to the Library Management System!          ")
    print("                     Choose an option:                      ")
    print("------------------------------------------------------------")
    print("                     1. Add a New Book                      ")
    print("                     2. Borrow a Book                       ")
    print("                     3. Return a Book                       ")
    print("                     4. View All Books                      ")
    print("                     5. Save & Exit                         ")
    print("------------------------------------------------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(title, author)
    elif choice == "2":
        title = input("Enter the book title to borrow: ")
        library.borrow_book(title)
    elif choice == "3":
        title = input("Enter the book title to return: ")
        library.return_book(title)
    elif choice == "4":
        library.view_books()
    elif choice == "5":
        library.save_and_exit()
        break
    else:
        print("Invalid choice. Please choose a number.\n")