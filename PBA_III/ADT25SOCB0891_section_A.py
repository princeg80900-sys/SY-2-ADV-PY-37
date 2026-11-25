class Bill:
    def __init__(self, customer_name, bill_number, bill_amount):
        self.customer_name = customer_name
        self.bill_number = bill_number
        self.amount = bill_amount

    def categorize_bill(self):
        if self.amount < 1000:
            return "Low Value"
        elif 1000 <= self.amount < 5000:
            return "Medium Value"
        else:
            return "High Value"

    def display_bill(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Bill Number: {self.bill_number}")
        print(f"Bill Amount: ₹{self.amount}")
        print(f"Bill Category: {self.categorize_bill()}")

class Pharmacy:
    def __init__(self):
        self.bills = []

    def adding_bill_records(self, bill):
        self.bills.append(bill)

    def display_all_bills(self):
        for bill in self.bills:
            bill.display_bill()
            print("-" * 30)

p = Pharmacy()
p.adding_bill_records(Bill("Chetan", 101, 750.00))
p.adding_bill_records(Bill("Aakash", 102, 2500.00))
p.adding_bill_records(Bill("Prince", 103, 6000.00))
p.display_all_bills()   

#output:
# Customer Name: Chetan
# Bill Number: 101
# Bill Amount: ₹750.0
# Bill Category: Low Value
# ------------------------------
# Customer Name: Aakash
# Bill Number: 102
# Bill Amount: ₹2500.0
# Bill Category: Medium Value
# ------------------------------
# Customer Name: Prince
# Bill Number: 103
# Bill Amount: ₹6000.0
# Bill Category: High Value
# ------------------------------

# OOP concepts used in this program:
# - Class: Bill and Pharmacy define the structure and behavior of objects.
# - Object: Each Bill(...) call creates a bill object; p is a Pharmacy object.
# - Encapsulation: Bill keeps related data (customer_name, bill_number, amount)
#   and operations (categorize_bill and display_bill) together.
# - Abstraction: display_bill() and display_all_bills() hide the details of
#   formatting and displaying records behind simple method calls.
# - Composition: Pharmacy stores and manages Bill objects in its bills list.

