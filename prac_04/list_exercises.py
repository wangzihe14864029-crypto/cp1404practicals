"""
CP1404 - Practical
"""

# Named constant
NUMBER_COUNT = 5

def main():
    """Run both the list operations and security checker."""
    numbers = get_numbers(NUMBER_COUNT)
    display_number_summary(numbers)
    check_user_access()


def get_numbers(count):
    """Get a list of numbers entered by the user."""
    numbers = []
    for i in range(count):
        number = float(input("Number: "))
        numbers.append(number)
    return numbers


def display_number_summary(numbers):
    """Display summary information about a list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}")


def check_user_access():
    """Check whether a username is authorised."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole',
        'InterpreterInterface', 'StartServer', 'bob'
    ]

    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
