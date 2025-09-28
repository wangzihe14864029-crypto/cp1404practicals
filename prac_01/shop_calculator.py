"""
CP1404 - Practical
Shop Calculator
"""

# Ask for the number of items, with input validation (must be >= 0)
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Accumulate the total price of all items
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply 10% discount if the total is greater than $100
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
