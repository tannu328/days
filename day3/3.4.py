def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return [even_sum, odd_sum]


numbers = [1,8,5,9,2,22,28,19]
result = sum_even_odd(numbers)
print(f"Sum of even numbers and odd numbers: {result}")
