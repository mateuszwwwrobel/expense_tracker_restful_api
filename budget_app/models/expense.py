from datetime import date


expenses = []


def next_id():
    """Function automatically assigns an id for the next created object."""
    if not expenses:
        return 1
    else:
        return expenses[-1].id + 1


class Expense:
    """Expense class"""

    def __init__(self, figure: int, person: str, category: str, currency='GBP', date=date.today()) -> None:
        """Constructor for Expense class."""
        self.id = next_id()
        self.figure = figure
        self.person = person
        self.category = category
        self.currency = currency
        self.date = date

    @property
    def data(self) -> dict:
        """Proper"""
        return {
            'id': self.id,
            'figure': self.figure,
            'person': self.person,
            'category': self.category,
            'currency': self.currency,
            'date': self.date.isoformat()
        }

    def __str__(self) -> str:
        return f"{self.date} - {self.figure}"
