"""
CP1404 - Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    display_income_report(incomes)


def display_income_report(incomes):
    """Display each month's income and cumulative total."""
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}  Total: ${total:10.2f}")


main()
