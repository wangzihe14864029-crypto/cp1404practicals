"""
CP1404 - Practical
Loops practice
"""

# a. count in 10s from 0 to 100
print("a.")
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b. count down from 20 to 1
print("b.")
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c. print a number of stars (all on one line)
print("c.")
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# d. print lines of increasing stars
print("d.")
number_of_lines = int(input("Number of lines: "))
for i in range(1, number_of_lines + 1):
    print("*" * i)
