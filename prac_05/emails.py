"""
CP1404 Practical
Store users' emails and names in a dictionary.
Estimate: 25 minutes
Actual: 28 minutes
"""

def main():
    """Store and display emails with associated names."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        # Prompt user to confirm the extracted name
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm != "" and confirm != "y":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    # Display all collected email-name pairs
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a user's name from their email address."""
    # Split the part before '@', then separate words by '.', capitalize each word
    name_part = email.split('@')[0]
    parts = name_part.split('.')
    name = " ".join(parts).title()
    return name


main()
