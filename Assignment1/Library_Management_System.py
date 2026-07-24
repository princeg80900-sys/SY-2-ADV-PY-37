class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        name = input("Enter Book Name: ")
        self.books.append(Book(name))
        print("Book Added Successfully.")

    def register_patron(self):
        name = input("Enter Patron Name: ")
        self.patrons.append(Patron(name))
        print("Patron Registered Successfully.")

    def borrow_book(self):
        name = input("Enter Book Name: ")
        for book in self.books:
            if book.name == name:
                if book.available:
                    book.available = False
                    print("Book Borrowed Successfully.")
                else:
                    print("Book is Already Borrowed.")
                return
        print("Book Not Found.")

    def return_book(self):
        name = input("Enter Book Name: ")
        for book in self.books:
            if book.name == name:
                if not book.available:
                    book.available = True
                    print("Book Returned Successfully.")
                else:
                    print("Book is Already Available.")
                return
        print("Book Not Found.")


library = Library()

while True:
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please Enter a Valid Number.")
        continue

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.register_patron()
    elif choice == 3:
        library.borrow_book()
    elif choice == 4:
        library.return_book()
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid Choice.")



# #OUTPUT:
# ----- Library Menu -----
# 1. Add Book
# 2. Register Patron
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter Your Choice: 1
# Enter Book Name: VEDAS
# Book Added Successfully.

# ----- Library Menu -----
# 1. Add Book
# 2. Register Patron
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter Your Choice: 2
# Enter Patron Name: Akash
# Patron Registered Successfully.

# ----- Library Menu -----
# 1. Add Book
# 2. Register Patron
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter Your Choice: 3
# Enter Book Name: VEDAS
# Book Borrowed Successfully.

# ----- Library Menu -----
# 1. Add Book
# 2. Register Patron
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter Your Choice: 4
# Enter Book Name: VEDAS
# Book Returned Successfully.

# ----- Library Menu -----
# 1. Add Book
# 2. Register Patron
# 3. Borrow Book
# 4. Return Book
# 5. Exit
# Enter Your Choice: 5
# Thank You!
