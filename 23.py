
from itertools import chain
abundants = []
def checkAbundant(n):
    factors = list(chain(*[[i, n//i] for i in range(1,int(n**0.5)+1) if n%i == 0]))
    factors = list(set(factors)) # remove duplicates e.g. squares
    factors.remove(n)
    total = sum(factors)
    if total > n:
        abundants.append(n)

for i in range(1, 28123+1):
    checkAbundant(i)

totals = [abundant+item for item in abundants for abundant in abundants] # sum all items

totals = set(totals) # quicker, ~O(1) instead of O(n)
nonsummables = [i for i in range(1, 28123+1) if i not in totals]
print(sum(nonsummables))

