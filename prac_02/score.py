"""
CP1404 - Practical
Program to determine score status
"""
import random


def main():
    """Ask the user for a score, print the result, and also test a random score."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score is {random_score} → {determine_result(random_score)}")


def determine_result(score):
    """Determine the result string for the given score and return it."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
