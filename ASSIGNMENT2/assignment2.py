def report_header(func):
def wrapper(*args, **kwargs):

print(&quot;=&quot; * 40)
print(&quot; STUDENT REPORT&quot;)
print(&quot;=&quot; * 40)
func(*args, **kwargs)
print(&quot;=&quot; * 40)
return wrapper

class Report:
college = &quot;ABC Engineering College&quot;

# Constructor (Magic Method)
def __init__(self, name, roll, marks):
self.name = name
self.roll = roll
self.marks = marks

# Class Method
@classmethod
def change_college(cls, new_name):
cls.college = new_name

# Magic Method
def __str__(self):
return f&quot;Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}&quot;

# Decorator applied to display report
@report_header
def display_report(self):
print(f&quot;College : {Report.college}&quot;)
print(self)
if self.marks &gt;= 40:
print(&quot;Result : PASS&quot;)
else:
print(&quot;Result : FAIL&quot;)

# Main Program
student1 = Report(&quot;Rahul&quot;, 101, 85)
student1.display_report()

print()

# Change college name using class method
Report.change_college(&quot;XYZ Institute of Technology&quot;)

student2 = Report(&quot;Priya&quot;, 102, 35)
student2.display_report()
