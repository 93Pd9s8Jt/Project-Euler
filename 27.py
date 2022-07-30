import time


def quadratic(n, a, b):
    return n**2 + a*n + b

def isPrime(x):
    if x in primes:
        return True
    else:
        prime = all(x % i for i in range(2, int(x ** 0.5) + 1))
        if prime:
            primes.add(x)
        return prime

primes = set()
maxcount = 0
maxformula = (0, 0)
for i in range(2,1000):
    isPrime(i)
bPrimes = primes.copy()
for a in range(-999, 1000, 2): # a must be odd
    for b in bPrimes: # b must be prime
        prime = True
        n = 0
        count = 0
        while prime:
            number = quadratic(n, a, b)
            if number < 2 or n >= b:
                break
            prime = isPrime(number)
            if prime:
                count += 1
                n += 1
        if count > maxcount:
            maxcount, maxformula = count, (a, b)
            

print(maxcount, maxformula)
