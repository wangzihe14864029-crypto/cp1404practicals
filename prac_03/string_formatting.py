"""
CP1404 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# The old manual way (not recommended)
print("My guitar: " + name + ", first made in " + str(year))

# Using str.format()
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Using f-strings (preferred)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency
print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

# Aligning columns with width
numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:>5}")

# TODO 1: f-string formatting
print(f"{year} {name} for about ${cost:,.0f}!")

# TODO 2: loop with f-string formatting
for i in range(0, 11):
    print(f"{2:>2} ^ {i:>2} is {2 ** i:>5}")
