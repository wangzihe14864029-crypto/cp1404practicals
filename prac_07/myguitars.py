"""
CP1404 Practical
More Guitars Program
Estimate: 20 minutes
Actual: 22 minutes
"""

from guitar import Guitar


def main():
    """Read guitars from file, sort them, display and allow user input."""
    guitars = load_guitars("guitars.csv")

    print("These are the existing guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort by year
    guitars.sort()

    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Add a new guitar
    print("\nAdd new guitars (blank name to stop):")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ").strip()

    # Save to file
    save_guitars("guitars.csv", guitars)
    print("\nAll guitars saved to guitars.csv")


def load_guitars(filename):
    """Read guitars from CSV file and return list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def save_guitars(filename, guitars):
    """Write all guitars back to CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
