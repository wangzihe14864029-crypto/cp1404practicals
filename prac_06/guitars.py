"""
CP1404 Practical - Guitars program
Estimate: 15 minutes
Actual: 16 minutes
"""

from guitar import Guitar

def main():
    """Program to store user’s guitars and display them."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    # For testing, comment out input and add hardcoded data like this:
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
