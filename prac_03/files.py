"""
CP1404/CP5632 - Practical
File reading and writing exercises
"""

# 1. Ask the user for their name and write it to a file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from the file and display a greeting
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read only the first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    result = number1 + number2
print(result)

# 4. Read all numbers from numbers.txt and print the total
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
print(total)