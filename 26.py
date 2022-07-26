
def getRecurring(denominator):
    decimal = []
    r = 1 
    while True:
        num = r // denominator

        r %= denominator
        if (num, r) == (0, 0):
            return (0, 0)
        if num == 0:
            r, r = 0, r*10
        else:
            if ([num,r]) in decimal:
                recurring = [item[0] for item in decimal[decimal.index([num, r]):]]
                return recurring
            decimal.append([num, r])
        
max = (0, 0)
for i in range(2, 1000):
    recurring = "".join(str(int) for int in getRecurring(i))
    if len(recurring)>max[0]:
        max = (len(recurring), i)
print(max[1])
