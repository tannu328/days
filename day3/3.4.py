#Write a function/program that takes a list of numbers and returns a list with two elements:
	#The first element should be the sum of all even numbers in the list.
	#The second element should be the sum of all odd numbers in the list.

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
