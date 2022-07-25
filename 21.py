from itertools import chain
createdict = True
def getFactorSum(n):
    if n in factorsums:
        return factorsums[n]
    factors = list(chain(*[[i, n//i] for i in range(1,int(n**0.5)+1) if n%i == 0]))
    list(set(factors)) # remove duplicates e.g. squares
    factors.remove(n)
    total = sum(factors)
    if createdict:
        factorsums[n] = total
    return total
factorsums = {}
for i in range(1,10000):
    getFactorSum(i)
createdict=False
amicables = [amicable for amicable in factorsums.keys() if getFactorSum(getFactorSum(amicable)) == amicable and getFactorSum(amicable) != amicable]

print(sum(amicables))
