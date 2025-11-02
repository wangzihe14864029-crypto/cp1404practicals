"""
CP1404 Practical - programming_language.py
Estimate: 20 minutes
Actual: 25 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing          # "Static" or "Dynamic"
        self.reflection = reflection  # True / False
        self.year = year

    def is_dynamic(self) -> bool:
        """Return True if this language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        """Return a nicely formatted string for printing."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
