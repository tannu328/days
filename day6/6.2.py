import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    
    def getArea(self):
        return math.pi * (self.radius ** 2)


    def getPerimeter(self):
        return 2 * math.pi * self.radius


circy = Circle(11)
print(circy.getArea())  

circy = Circle(4.44)
print(circy.getPerimeter())
