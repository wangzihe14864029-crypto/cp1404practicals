"""
CP1404 - Practical
Random number examples.
"""

import random

print(random.randint(5, 20))  # Smallest possible: 5, Largest possible: 20
print(random.randrange(3, 10, 2))  # Smallest possible: 3, Largest possible: 9, 4 not possible
print(random.uniform(2.5, 5.5))  # Smallest possible: 2.5, Largest possible: 5.5
print(random.randint(1, 100))  # Random number between 1 and 100 inclusive
