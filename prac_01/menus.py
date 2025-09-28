"""
CP1404 - Practical
Menu-driven program example
"""

# Get user's name
name = input("Enter name: ")

# Display the menu
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)

# Get initial choice
choice = input(">>> ").upper()

# Loop until the user chooses Q
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Re-display menu and get new choice
    print(MENU)
    choice = input(">>> ").upper()

# Exit message
print("Finished.")
