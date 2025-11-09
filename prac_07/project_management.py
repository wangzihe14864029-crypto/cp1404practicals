"""
CP1404 Practical - Do-from-scratch: Project Management Program

Estimate: 80 minutes
Actual: 77 minutes
"""
from __future__ import annotations
from datetime import datetime, date
from typing import List

from project import Project, DATE_FMT

DEFAULT_FILE = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main() -> None:
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == "l":
            filename = input("Filename to load from: ").strip() or DEFAULT_FILE
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save to: ").strip() or DEFAULT_FILE
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            after = prompt_date("Show projects that start after date (dd/mm/yy): ")
            show_after(projects, after)
        elif choice == "a":
            projects.append(prompt_new_project())
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            ask_save_default_on_quit(projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


# ---------- File IO ----------

def load_projects(filename: str) -> List[Project]:
    """Load projects from a tab-delimited file (skip the header)."""
    projects: List[Project] = []
    with open(filename, "r", encoding="utf-8") as in_file:
        header = in_file.readline()  # ignore header
        for line in in_file:
            if line.strip():
                projects.append(Project.from_tab_line(line))
    return projects


def save_projects(filename: str, projects: List[Project]) -> None:
    """Save projects to a tab-delimited file with header."""
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            out_file.write(p.to_tab_line() + "\n")


def ask_save_default_on_quit(projects: List[Project]) -> None:
    """Ask the user whether to save to default file on quit."""
    response = input(f"Would you like to save to {DEFAULT_FILE}? ").strip().lower()
    if response and response[0] == "y":
        save_projects(DEFAULT_FILE, projects)
    else:
        print("no, I think not.")


# ---------- Display & Queries ----------

def display_projects(projects: List[Project]) -> None:
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def show_after(projects: List[Project], after: date) -> None:
    """Display projects that start after a given date, sorted by date."""
    filtered = sorted([p for p in projects if p.start_date > after],
                      key=lambda p: p.start_date)
    for p in filtered:
        print(p)


# ---------- Add & Update ----------

def prompt_new_project() -> Project:
    """Prompt the user for project fields and return a Project."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    start = prompt_date("Start date (dd/mm/yy): ")
    priority = prompt_int("Priority: ")
    cost = prompt_float("Cost estimate: $")
    percent = prompt_int("Percent complete: ")
    return Project(priority=priority, name=name, start_date=start,
                   cost_estimate=cost, percent_complete=percent)


def update_project(projects: List[Project]) -> None:
    """Let the user choose a project then update percent and/or priority."""
    sorted_projects = sorted(projects)
    for i, p in enumerate(sorted_projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: "))
    except ValueError:
        print("Invalid selection")
        return
    if not (0 <= index < len(sorted_projects)):
        print("Invalid selection")
        return
    project = sorted_projects[index]
    # Find the same object reference in the original list
    real_index = projects.index(project)

    new_percent_text = input("New Percentage: ").strip()
    if new_percent_text != "":
        projects[real_index].percent_complete = clamp_int(new_percent_text, 0, 100)

    new_priority_text = input("New Priority: ").strip()
    if new_priority_text != "":
        projects[real_index].priority = int(new_priority_text)


# ---------- Input helpers ----------

def prompt_date(prompt: str) -> date:
    """Prompt for a date in dd/mm/yy (or yyyy) and return a date object."""
    while True:
        text = input(prompt).strip()
        for fmt in ("%d/%m/%y", DATE_FMT):
            try:
                return datetime.strptime(text, fmt).date()
            except ValueError:
                pass
        print("Invalid date, try again (e.g., 20/7/2022)")


def prompt_int(prompt: str) -> int:
    """Prompt for an integer and return it."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number, try again")


def prompt_float(prompt: str) -> float:
    """Prompt for a float and return it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again")


def clamp_int(text: str, low: int, high: int) -> int:
    """Convert text to int and clamp between [low, high]."""
    try:
        value = int(text)
    except ValueError:
        value = low
    return max(low, min(high, value))


if __name__ == "__main__":
    main()
