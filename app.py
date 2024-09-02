import random
class Event:
    def __init__(self, name, venue, date, categories):
        self.name = name
        self.venue = venue
        self.date = date
        self.categories = categories  # Dictionary to store ticket categories and available seats

    def display_details(self):
        print("Event:", self.name)
        print("Venue:", self.venue)
        print("Date:", self.date)
        print("Categories:", self.categories)
        print()

    def book_tickets(self, category, num_tickets):
        if category in self.categories:
            available_seats = self.categories[category]
            if num_tickets <= available_seats:
                print(f"Booking {num_tickets} tickets for {self.name} - {category} category...")
                self.categories[category] -= num_tickets
                print("Booking successful!")
                print(f"Total amount due: {num_tickets * self.get_price(category)}")
            else:
                print(f"Sorry, only {available_seats} seats available for {category} category.")
        else:
            print("Invalid category.")

    def get_price(self, category):
        # Placeholder function to calculate ticket price based on category
        return random.randint(20, 50)
class TicketBookingSystem:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def display_events(self):
        print("Available Events:")
        for index, event in enumerate(self.events, start=1):
            print(f"{index}. {event.name}")

    def book_tickets(self, event_index, category, num_tickets):
        event = self.events[event_index]
        event.book_tickets(category, num_tickets)
def main():
    # Create TicketBookingSystem instance
    booking_system = TicketBookingSystem()

    # Create some events
    event1 = Event("Concert", "City Hall", "2024-05-15", {"VIP": 100, "General": 200})
    event2 = Event("Movie Premiere", "Cinema World", "2024-06-10", {"Premium": 50, "Standard": 100})

    # Add events to booking system
    booking_system.add_event(event1)
    booking_system.add_event(event2)

    # Display available events
    booking_system.display_events()

    # Prompt user to select an event
    event_index = int(input("Enter the event number you want to book: ")) - 1

    # Check if the event index is valid
    if 0 <= event_index < len(booking_system.events):
        event = booking_system.events[event_index]
        print(f"Available categories for {event.name}: {list(event.categories.keys())}")

        category = input("Enter the category you want to book: ")
        num_tickets = int(input("Enter the number of tickets you want to book: "))
        booking_system.book_tickets(event_index, category, num_tickets)
    else:
        print("Invalid event number. Please try again.")

if __name__ == "__main__":
    main()
