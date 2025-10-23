"""
CP1404 Practical - Wimbledon data processing
Estimate: 40 minutes
Actual: 48 minutes
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """Process the Wimbledon CSV and display champions and countries."""
    rows = load_wimbledon_data(FILENAME)
    champion_to_wins = count_champions(rows)
    countries = collect_countries(rows)

    print("Wimbledon Champions:")
    display_champions(champion_to_wins)
    print()
    display_countries(countries)


def load_wimbledon_data(filename):
    """Load CSV rows."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header
        return [row for row in reader]


def count_champions(rows):
    """Return dict mapping champion name -> number of wins."""
    champion_to_wins = {}
    for row in rows:
        champion = row[2]  # 第三列是冠军名字
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def collect_countries(rows):
    """Return a set of countries that have produced champions."""
    return {row[1] for row in rows}  # 第二列是国家


def display_champions(champion_to_wins):
    """Print champions and win counts."""
    for champion in sorted(champion_to_wins):
        print(f"{champion} {champion_to_wins[champion]}")


def display_countries(countries):
    """Print countries in alphabetical order."""
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


if __name__ == "__main__":
    main()
