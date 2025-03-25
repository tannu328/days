#Create a function/input that, given a number, returns the corresponding value of that index in the Fibonacci series.


def fibo(n):

    if n == 0 or n == 1:
        return 1
    

    a, b = 1, 1
    

    for i in range(2, n+1):
        a, b = b, a + b
    
    return b

print(fibo(0))
print(fibo(1))
print(fibo(5))  
print(fibo(10)) 
