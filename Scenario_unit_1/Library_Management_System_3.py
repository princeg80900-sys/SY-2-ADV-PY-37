class Book:

    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Premium"
        else:
            return "Standard"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Price:", book.price)
            print("Category:", book.category())
            print("----------------")


b1 = Book(1, "Python", "Guido", 1200)
b2 = Book(2, "C Programming", "Dennis", 500)

library = Library()

library.add_book(b1)
library.add_book(b2)

library.display_books()

# OUTPUT:
#---------------
# Book ID: 1
# Title: Python
# Author: Guido
# Price: 1200
# Category: Premium
# ----------------
# Book ID: 2
# Title: C Programming
# Author: Dennis
# Price: 500
# Category: Standard
# ----------------
