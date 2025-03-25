#Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

def people_sort(people, attribute):
    
    return sorted(people, key=lambda person: getattr(person, attribute))


p1 = Person("tanvi", "taraviya", 20)
p2 = Person("krishna", "chovtiya", 21)
p3 = Person("devyani", "vekariya", 21)


sorted_by_firstname = people_sort([p1, p2, p3], "firstname")
sorted_by_lastname = people_sort([p1, p2, p3], "lastname")
sorted_by_age = people_sort([p1, p2, p3], "age")


print([p.firstname for p in sorted_by_firstname])
print([p.lastname for p in sorted_by_lastname])    
print([p.age for p in sorted_by_age])             
