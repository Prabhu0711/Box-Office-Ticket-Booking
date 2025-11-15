# Simple Box Office Ticket Booking System

movies = {
    "1": {"name": "Jawan", "price": 150, "seats": 50},
    "2": {"name": "Salaar", "price": 180, "seats": 40},
    "3": {"name": "Leo", "price": 200, "seats": 30}
}

def show_movies():
    print("\n----- Now Showing -----")
    for key, movie in movies.items():
        print(f"{key}. {movie['name']} - Ticket ₹{movie['price']} - Seats left: {movie['seats']}")

def book_ticket():
    show_movies()
    choice = input("\nChoose a movie number: ")

    if choice not in movies:
        print("Invalid choice! Try again.")
        return

    movie = movies[choice]

    try:
        count = int(input("How many tickets do you want to book? "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if count <= 0:
        print("Ticket count must be greater than 0.")
        return

    if count > movie["seats"]:
        print("Not enough seats available!")
        return

    # Payment calculation
    total_cost = count * movie["price"]

    movie["seats"] -= count
    print(f"\n🎉 Booking Successful!")
    print(f"Movie: {movie['name']}")
    print(f"Tickets: {count}")
    print(f"Total Amount: ₹{total_cost}")
    print("Enjoy your movie! 🍿")

def main():
    while True:
        print("\n----- BOX OFFICE SYSTEM -----")
        print("1. View Movies")
        print("2. Book Tickets")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Thank you for using Box Office! 🎬")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
main()
