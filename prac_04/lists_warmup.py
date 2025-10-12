"""
CP1404 - Practical
"""

# Named constants
FIRST_INDEX = 0
LAST_INDEX = -1
SLICE_START_INDEX = 2
SEARCH_NUMBER = 9

def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]

    # Predicted values
    # numbers[0] -> 3
    # numbers[-1] -> 2
    # numbers[3] -> 1
    # numbers[::-1] -> [2, 9, 5, 1, 4, 1, 3]
    # numbers[3:4] -> [1]
    # 5 in numbers -> True
    # 7 in numbers -> False
    # "3" in numbers -> False
    # numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    numbers[FIRST_INDEX] = "ten"
    numbers[LAST_INDEX] = 1
    print(numbers[SLICE_START_INDEX:])
    print(SEARCH_NUMBER in numbers)


main()

