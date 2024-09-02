# ticket
Ticket Booking System

The Ticket Booking System is a Python-based application designed to manage and facilitate the booking of tickets for various events. This project provides a simple command-line interface where users can view available events, select ticket categories, and book tickets. The system supports multiple events and ticket categories with dynamic pricing and seat availability.

Features
Event Management: Create and manage multiple events with details such as name, venue, date, and ticket categories.
Category-Based Booking: Book tickets for specific categories within an event, with real-time seat availability checks.
Dynamic Pricing: Calculate ticket prices dynamically based on predefined logic.
Command-Line Interface: Interact with the system via a simple command-line interface to select events and book tickets.

Classes
Event
Attributes:
name: Name of the event.
venue: Venue of the event.
date: Date of the event.
categories: Dictionary storing ticket categories and the number of available seats.
Methods:
display_details(): Displays event details including name, venue, date, and categories.
book_tickets(category, num_tickets): Books tickets for a specified category, updating the available seats and calculating the total amount due.
get_price(category): Returns the price of a ticket based on the category (currently a placeholder for dynamic pricing).

TicketBookingSystem
Attributes:
events: List of Event objects.
Methods:
add_event(event): Adds an event to the booking system.
display_events(): Displays a list of available events.
book_tickets(event_index, category, num_tickets): Books tickets for a specified event, category, and number of tickets.

Feel free to submit pull requests or open issues for improvements or bug fixes.


