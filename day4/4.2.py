#Create a function/input that counts the integer's number of digits.Solve this without using strings.


def count_digits(n):

    if n == 0:
        return 1
    

    if n < 0:
        n = -n
    
    digit_count = 0
    

    while n > 0:
        n //= 10
        digit_count += 1
    
    return digit_count


number = 856327
result = count_digits(number)
print(f"The number of digits in {number} is: {result}")
