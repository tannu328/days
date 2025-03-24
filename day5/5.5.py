def is_prime(n):

    if n <= 1:
        return False
   
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):

    if is_prime(n):
        return n

    while True:
        n += 1
        if is_prime(n):
            return n


print(next_prime(5))
print(next_prime(10))
print(next_prime(14)) 
print(next_prime(1))  
