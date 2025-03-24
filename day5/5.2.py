def calculate(num1, num2, op):

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":

        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operator"


print(calculate(10, 5, "+"))  
print(calculate(10, 5, "-"))  
print(calculate(10, 5, "*"))  
print(calculate(10, 5, "/"))  
print(calculate(10, 0, "/"))  
print(calculate(10, 5, "^"))  
