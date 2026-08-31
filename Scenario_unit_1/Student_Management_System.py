class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def assign_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display_details(self):
        print("Roll Number :", self.roll_number)
        print("Name        :", self.name)
        print("Marks       :", self.marks)
        print("Grade       :", self.assign_grade())
        print("-" * 35)


class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        print("\n" + "=" * 45)
        print(self.college_name)
        print("STUDENT DETAILS")
        print("=" * 45)

        for student in self.students:
            student.display_details()


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


print("===== STUDENT MANAGEMENT SYSTEM =====")

college_name = input("Enter College Name: ")
college = College(college_name)

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = Student(roll_number, name, marks)
    college.add_student(student)

college.display_all_students()


print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")

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

# ===== STUDENT MANAGEMENT SYSTEM =====
# Enter College Name: MIT ADT University
# Enter number of students: 3
#
# Enter details of Student 1
# Enter Roll Number: 101
# Enter Name: Prince
# Enter Marks: 96
#
# Enter details of Student 2
# Enter Roll Number: 102
# Enter Name: Saniya
# Enter Marks: 78
#
# Enter details of Student 3
# Enter Roll Number: 103
# Enter Name: Himanshu
# Enter Marks: 69
#
# =============================================
# MIT ADT University
# STUDENT DETAILS
# =============================================
# Roll Number : 101
# Name        : Prince
# Marks       : 96.0
# Grade       : A
# -----------------------------------
# Roll Number : 102
# Name        : Saniya
# Marks       : 78.0
# Grade       : B
# -----------------------------------
# Roll Number : 103
# Name        : Himanshu
# Marks       : 69.0
# Grade       : C
# -----------------------------------
#
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
