#Write a Program that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.
import math 
def calculate(x1,y1,x2,y2):
    distance = math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)
    return distance 
x1 = float(input("enter value x1"))
y1 = float(input("enter value y1"))
x2 = float(input("enter value x2"))
y2 = float(input("enter value y2"))

distance = calculate(x1,y1,y2,x2)
print (f"the length of the line :{distance}")