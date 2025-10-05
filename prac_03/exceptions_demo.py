"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user enters a non-integer input.
2. When will a ZeroDivisionError occur?
When the user enters 0 as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by checking that the denominator is not zero before dividing.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator again: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
