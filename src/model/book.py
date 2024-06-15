class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {self.price})"
