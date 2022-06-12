a = 1
b = 1
new = a+b
sum = 0
while new < 4000000:
    # every 3rd fibbonachi is even
    sum += new
    a = b+new
    b = a+new
    new = a+b
print(sum)
