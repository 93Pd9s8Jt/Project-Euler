power = {}
for i in range(10):
    power[i] = i**5
numsum = 0
for i in range(1,1000000):
    total = sum([power[int(x)] for x in str(i)])
    if total == i:
        numsum +=i
print(numsum-1)
