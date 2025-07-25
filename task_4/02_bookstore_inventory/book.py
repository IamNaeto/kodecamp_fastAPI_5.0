class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(price, 2)
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["price"],
            data["stock"]
        )
