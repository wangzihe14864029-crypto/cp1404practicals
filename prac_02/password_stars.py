def main():
    """Run the password check program."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get a valid password from the user and return it."""
    password = input("Enter your password: ")
    while len(password) < 4:
        print("Password must be at least 4 characters long")
        password = input("Enter your password: ")
    return password


def print_stars(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))


main()
