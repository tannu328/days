#Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:Form the fullname by simply joining the first and last name together, separated by a space.Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = f"{first} {last}"
        self.email = f"{first.lower()}.{last.lower()}@company.com"


emp_1 = Employee("tanvi", "taraviya")
emp_2 = Employee("tanvi", "taraviya")
emp_3 = Employee("yashraj", "paramar")


print(emp_1.fullname)  
print(emp_2.email)    
print(emp_3.first)     
