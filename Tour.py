# Tour Management System
tours = {
    1: {"name": "Ooty Tour", "price": 5000},
    2: {"name": "Kodaikanal Tour", "price": 6000},
    3: {"name": "Goa Tour", "price": 12000},
    4: {"name": "Kerala Tour", "price": 10000}
}
bookings = []
def display_tours():
    print("\nAvailable Tour Packages")
    print("-" * 30)
    for tour_id, details in tours.items():
        print(f"{tour_id}. {details['name']} - ₹{details['price']}")
def book_tour():
    display_tours()
    try:
        choice = int(input("\nEnter Tour ID to Book: "))
        if choice in tours:
            name = input("Enter Customer Name: ")
            booking = {
                "customer": name,
                "tour": tours[choice]["name"],
                "price": tours[choice]["price"]
            }
            bookings.append(booking)
            print("\nTour Booked Successfully!")
        else:
            print("Invalid Tour ID.")
    except ValueError:
        print("Please enter a valid number.")
def view_bookings():
    if not bookings:
        print("\nNo bookings found.")
        return
    print("\nBooked Tours")
    print("-" * 40)
    for i, booking in enumerate(bookings, start=1):
        print(f"{i}. Customer: {booking['customer']}")
        print(f"   Tour: {booking['tour']}")
        print(f"   Price: ₹{booking['price']}")
        print()
def cancel_booking():
    view_bookings()
    if not bookings:
        return
    try:
        booking_no = int(input("Enter Booking Number to Cancel: "))
        if 1 <= booking_no <= len(bookings):
            removed = bookings.pop(booking_no - 1)
            print(f"\nBooking for {removed['customer']} cancelled successfully.")
        else:
            print("Invalid booking number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    while True:
        print("\n===== TOUR MANAGEMENT SYSTEM =====")
        print("1. View Tour Packages")
        print("2. Book Tour")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tours()
        elif choice == "2":
            book_tour()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Thank you for using Tour Management System!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
