#Create a program that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive
def sum(a,b,c):
    total=0
    for num in range(a,b+1):
        if num % c ==0:
            total +=num
    return total 
a = int (input("enter value a:"))
b = int (input("enter value b:"))
c = int (input("enter value c:"))

result = sum (a,b,c)
print (f"the sub divisible {c} in range {a} to {b} is : {result}")