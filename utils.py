def get_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * get_factorial(n - 1)

def is_power_of_five(n):
    if n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
