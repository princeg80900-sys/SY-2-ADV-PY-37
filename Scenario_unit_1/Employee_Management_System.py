class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def categorize_salary(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display_details(self):
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      : ₹", self.salary)
        print("Category    :", self.categorize_salary())
        print("-" * 35)


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        print("\n" + "=" * 45)
        print(self.company_name)
        print("EMPLOYEE INFORMATION")
        print("=" * 45)

        for employee in self.employees:
            employee.display_details()


print("===== EMPLOYEE MANAGEMENT SYSTEM =====")

company_name = input("Enter Company Name: ")
company = Company(company_name)

n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details of Employee {i + 1}")
    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(employee_id, name, salary)
    company.add_employee(employee)

company.display_all_employees()


# OUTPUT

# ===== EMPLOYEE MANAGEMENT SYSTEM =====
# Enter Company Name: ALL CODE Solutions Pvt. Ltd.
# Enter number of employees: 3
#
# Enter details of Employee 1
# Enter Employee ID: 101
# Enter Name: MAYA
# Enter Salary: 88000
#
# Enter details of Employee 2
# Enter Employee ID: 102
# Enter Name: RIYA
# Enter Salary: 54000
#
# Enter details of Employee 3
# Enter Employee ID: 103
# Enter Name: NAMAN
# Enter Salary: 38000
#
# =============================================
# ALL CODE Solutions Pvt. Ltd.
# EMPLOYEE INFORMATION
# =============================================
# Employee ID : 101
# Name        : MAYA
# Salary      : ₹ 88000.0
# Category    : High Salary
# -----------------------------------
# Employee ID : 102
# Name        : RIYA
# Salary      : ₹ 54000.0
# Category    : Medium Salary
# -----------------------------------
# Employee ID : 103
# Name        : NAMAN
# Salary      : ₹ 38000.0
# Category    : Low Salary
# -----------------------------------
