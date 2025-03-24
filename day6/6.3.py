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
