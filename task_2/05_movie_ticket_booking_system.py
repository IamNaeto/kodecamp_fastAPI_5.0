# Task 5: Movie Ticket Booking System

# Scenario: Manage ticket booking for a cinema.

# Instructions:

# - Show movie options with available seats and ticket price (dictionary)

# - Allow users to:

#  - Book a ticket (reduce seat count)

#  - View movies and seats

#  - Exit

# - Validate:

#  - That the movie exists

#  - That enough seats are available

# - Use functions, loops, error handling, and data structures


movies = {
    "Avatar": {"seats": 5, "price": 10},
    "Oppenheimer": {"seats": 3, "price": 12},
    "Barbie": {"seats": 4, "price": 8}
}

def view_movies():
    print("Available Movies:")
    for name, info in movies.items():
        print(f"{name} - Seats: {info['seats']} - Price: ${info['price']}")
    print()

def book_ticket():
    movie = input("Enter movie name: ").title()
    if movie in movies:
        try:
            quantity = int(input("Enter number of tickets: "))
            if quantity <= movies[movie]["seats"]:
                movies[movie]["seats"] -= quantity
                total = quantity * movies[movie]["price"]
                print(f"Booked {quantity} ticket(s) for {movie}. Total: ${total}\n")
            else:
                print("Not enough seats available.\n")
        except ValueError:
            print("Invalid quantity.\n")
    else:
        print("Movie not found.\n")

while True:
    print("1. View Movies\n2. Book Ticket\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        view_movies()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        break
    else:
        print("Invalid option.\n")
