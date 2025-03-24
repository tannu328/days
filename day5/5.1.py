import math

def radians_to_degrees(radians):

    degrees = radians * (180 / math.pi)
    

    return round(degrees, 1)


print(radians_to_degrees(2))
print(radians_to_degrees(math.pi))  
print(radians_to_degrees(4))  
