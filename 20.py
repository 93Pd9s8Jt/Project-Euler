import math
num = math.factorial(100)
total=0
for digit in str(num):
    total+=int(digit) 
print(total)
