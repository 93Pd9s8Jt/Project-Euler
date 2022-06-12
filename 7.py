primes = [2]
i=2
while len(primes) != 10001:
    is_prime = True
    i+=1
    for prime in primes:
        if i%prime == 0:
            is_prime = False
    if is_prime:
        primes.append(i)

print(primes[10000])
