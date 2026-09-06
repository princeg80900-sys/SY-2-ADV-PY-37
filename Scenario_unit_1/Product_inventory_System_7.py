class Product:

    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def category(self):
        if self.price >= 10000:
            return "Expensive"
        else:
            return "Affordable"


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print("Product ID:", product.product_id)
            print("Product Name:", product.product_name)
            print("Price:", product.price)
            print("Category:", product.category())
            print("----------------")


p1 = Product(1, "Laptop", 60000)
p2 = Product(2, "Mouse", 500)

inventory = Inventory()

inventory.add_product(p1)
inventory.add_product(p2)

inventory.display_products()

# OUTPUT:
#----------------
# Product ID: 1
# Product Name: Laptop
# Price: 60000
# Category: Expensive
# ----------------
# Product ID: 2
# Product Name: Mouse
# Price: 500
# Category: Affordable
# ----------------
