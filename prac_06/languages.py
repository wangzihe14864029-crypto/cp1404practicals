"""
CP1404 Practical - languages.py
Estimate: 20 minutes
Actual: 22 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create languages, print one, then list the dynamically typed ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()