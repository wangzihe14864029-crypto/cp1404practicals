"""
CP1404 - Practical
Menu program for score
"""
from score import determine_result


def main():
    """Run the score menu program with options for user score."""
    score = get_valid_score()
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print('*' * int(score))
        else:
            print("Invalid option")
        choice = display_menu()
    print("See you!")


def display_menu():
    """Display the menu and get the user's choice."""
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    return input(">>> ").upper()


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


main()