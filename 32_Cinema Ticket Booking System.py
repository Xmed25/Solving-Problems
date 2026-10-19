# Cinema Ticket Booking System

# Problem: Create a ticket booking program that calculates prices based on age, ticket type, number of tickets, and available discounts.

# Requirements
# - Accept the customer's name, age, ticket type, and number of tickets.
# - Support Standard, Premium, and VIP tickets.
# - Apply age-based discounts for children and seniors.
# - Apply a group discount when a booking meets a specified ticket threshold.
# - Prevent invalid ticket counts and unsupported ticket types.
# - Use membership operators to validate ticket categories.
# - Print a detailed receipt containing the original price, discount, and final total.
# Pricing rules
# Ticket type	Price
# Standard	100 EGP
# Premium	175 EGP
# VIP	250 EGP
# Additional rules: children under 12 receive 30% off; customers aged 60 or above receive 20% off. A booking of 5 or more tickets receives a 10% group discount. Discounts are applied sequentially: age discount first, then group discount.

# Example
# Customer: Alex
# Age: 20
# Ticket type: Premium
# Quantity: 2

# Original total: 350.00 EGP
# Age discount: 0.00 EGP
# Group discount: 0.00 EGP
# Final total: 350.00 EGP










def information():
    while True:
        name = input("Name: ").strip().title()

        if name:
            break

        print("Invalid Name. Try again.")

    while True:
        try:
            age = int(input("Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid Age. Enter a number.")

    print(
        "Children under 12 receive 30% off; "
        "customers aged 60 or above receive 20% off."
    )

    return name, age


def tickets(age):
    prices = {
        "standard": 100,
        "premium": 175,
        "vip": 250
    }

    print("\nTicket Types with Prices...")
    print("Standard: 100 EGP")
    print("Premium: 175 EGP")
    print("VIP: 250 EGP")

    while True:
        ticket = input("Ticket Type: ").strip().lower()

        if ticket in prices:
            break

        print("Invalid ticket type. Try again.")

    while True:
        try:
            num_tick = int(input("Number of Tickets: "))

            if num_tick <= 0:
                print("Enter a positive number.")
                continue

            break

        except ValueError:
            print("Invalid quantity. Enter a number.")

    original_total = prices[ticket] * num_tick

    discount_rate = 0

    if age < 12:
        discount_rate = 0.30
    elif age >= 60:
        discount_rate = 0.20

    discount = original_total * discount_rate
    final_total = original_total - discount

    return ticket, num_tick, original_total, discount, final_total


def displaying(name, age, ticket, num_tick,
               original_total, discount, final_total):

    print("\n--- Booking Summary ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Ticket Type: {ticket.title()}")
    print(f"Quantity: {num_tick}")
    print(f"Original Total: {original_total:.2f} EGP")
    print(f"Age Discount: {discount:.2f} EGP")
    print(f"Final Total: {final_total:.2f} EGP")


def main():
    name, age = information()

    ticket, num_tick, original_total, discount, final_total = (
        tickets(age)
    )

    displaying(
        name, age, ticket, num_tick,
        original_total, discount, final_total
    )


main()
