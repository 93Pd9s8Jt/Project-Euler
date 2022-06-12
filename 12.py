from functools import reduce
from math import sqrt

# ref https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
                    
def get_triangle_numbers():
    prev = 0
    t = 1
    i=1
    while True:
        yield t
        prev=t
        i+=1
        t=prev+i
        
        

triangle_numbers = get_triangle_numbers() # gen

num_factors = 0
while num_factors <= 500:   
    number = next(triangle_numbers)
    num_factors = len(factors(number))
print(number)
