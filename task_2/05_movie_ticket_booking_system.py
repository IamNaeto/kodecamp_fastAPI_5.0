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
    "Avengers": {"price": 15, "seats": 20},
    "Barbie": {"price": 12, "seats": 15},
    "Oppenheimer": {"price": 18, "seats": 10}
}

def view_movies():
    print("Movies Available:")
    for i, (name, data) in enumerate(movies.items(), 1):
        print(f"{i}. {name} - ${data['price']} - {data['seats']} seats left")
    print()

def book_ticket():
    movie = input("Enter movie name: ").title()
    if movie in movies:
        try:
            qty = int(input("How many tickets?: "))
            if qty <= movies[movie]['seats']:
                total = qty * movies[movie]['price']
                movies[movie]['seats'] -= qty
                print(f"Booking successful! You paid ${total}\n{movies[movie]['seats']} seats remaining.\n")
            else:
                print("Error: Not enough seats available.\n")
        except:
            print("Invalid quantity.\n")
    else:
        print("Movie not found.\n")

while True:
    print("1. Book Ticket\n2. View Movies\n3. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1": book_ticket()
    elif choice == "2":
        print("Movies Available:")
        for name, data in movies.items():
            print(f"- {name}: ${data['price']} ({data['seats']} seats left)")
        print()
    elif choice == "3": break
    else: print("Invalid option.\n")
