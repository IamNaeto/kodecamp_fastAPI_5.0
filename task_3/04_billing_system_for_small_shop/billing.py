import json
import os
import math
from datetime import datetime

FILENAME = os.path.join(os.path.dirname(__file__), "bills.json")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total()
        }

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, name, price, quantity):
        self.items.append(Product(name, price, quantity))
        print(f"Added {quantity} x {name} to cart.\n")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.\n")
            return
        print("--- Cart Contents ---")
        total = 0
        for item in self.items:
            print(f"{item.name} x{item.quantity} - ₦{item.total():.2f}")
            total += item.total()
        total = math.ceil(total)
        if total > 10000:
            discount = total * 0.1
            total -= discount
            print(f"Discount applied: ₦{discount:.2f}")
        print(f"Total: ₦{total:.2f}\n")

    def checkout(self):
        if not self.items:
            print("Cart is empty.\n")
            return
        bill = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": [item.to_dict() for item in self.items],
            "total": math.ceil(sum(item.total() for item in self.items))
        }
        if bill["total"] > 10000:
            discount = bill["total"] * 0.1
            bill["total"] -= discount
        self.save_bill(bill)
        print("Bill saved successfully.\n")
        self.items = []

    def save_bill(self, bill):
        bills = self.load_bills()
        bills.append(bill)
        with open(FILENAME, 'w') as f:
            json.dump(bills, f, indent=4)

    def load_bills(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, 'r') as f:
                return json.load(f)
        return []

    def view_history(self):
        history = self.load_bills()
        if not history:
            print("No previous transactions found.\n")
            return
        print("--- Previous Bills ---")
        for bill in history:
            print(f"Date: {bill['timestamp']}")
            for item in bill['items']:
                print(f" - {item['name']} x{item['quantity']} - ₦{item['total']:.2f}")
            print(f"Total: ₦{bill['total']:.2f}\n")
