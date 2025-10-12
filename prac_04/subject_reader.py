"""
CP1404 - Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display formatted details."""
    subject_data = load_subject_data(FILENAME)
    display_subject_details(subject_data)


def load_subject_data(filename):
    """Read data from file and return a list of [subject, lecturer, number_of_students]."""
    subject_records = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student number to int
            subject_records.append(parts)
    return subject_records


def display_subject_details(subject_records):
    """Display each subject’s details in a formatted sentence."""
    for record in subject_records:
        subject_code, lecturer_name, student_count = record
        print(f"{subject_code} is taught by {lecturer_name} and has {student_count} students")


main()
