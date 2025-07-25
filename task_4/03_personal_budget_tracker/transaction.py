from datetime import datetime

class Transaction:
    def __init__(self, date, category, amount):
        self.date = date  # string format: 'YYYY-MM-DD'
        self.category = category
        self.amount = round(amount, 2)

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data):
        return Transaction(data["date"], data["category"], data["amount"])
