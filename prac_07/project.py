"""
Project class used by project_management.py

Estimate: 40 minutes
Actual: 35 minutes
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime


DATE_FMT = "%d/%m/%Y"  # e.g., "12/09/2021"


@dataclass(order=True)
class Project:
    """Represent a project object."""
    # dataclass order=True
    priority: int
    name: str
    start_date: date
    cost_estimate: float
    percent_complete: int

    # The default order of dataclass is based on the field order;
    # we would like to prioritize by priority first, and then by start_date.
    # So put "priority" first; the rest can be in any order and have nothing to do with the display.

    def __str__(self) -> str:
        """Return a nice string for display."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FMT)}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.percent_complete}%")

    def is_complete(self) -> bool:
        """Return True if project is completed (100%)."""
        return self.percent_complete >= 100

    @classmethod
    def from_tab_line(cls, line: str) -> "Project":
        """Create a Project from a tab-delimited data line (ignoring header)."""
        # Name	Start Date	Priority	Cost Estimate	Completion Percentage
        parts = [p.strip() for p in line.strip().split("\t")]
        name = parts[0]
        start = datetime.strptime(parts[1], DATE_FMT).date()
        priority = int(parts[2])
        cost = float(parts[3])
        percent = int(parts[4])
        return cls(priority=priority, name=name, start_date=start,
                   cost_estimate=cost, percent_complete=percent)

    def to_tab_line(self) -> str:
        """Return a tab-delimited line matching the file format (no trailing tab)."""
        return "\t".join([
            self.name,
            self.start_date.strftime(DATE_FMT),
            str(self.priority),
            f"{self.cost_estimate}",
            str(self.percent_complete),
        ])