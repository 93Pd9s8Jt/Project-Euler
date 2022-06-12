def Collatz(n,count=1):
    if n in Collatz_dict:
        return Collatz_dict[str(n)]
    if n%2==0:
        n /= 2
    else:
        n = 3*n+1
    count+=1
    if n == 1:
        return count
    else:
        return Collatz(n,count)
Collatz_dict = {}

max = [0,0] # n,count
for i in range(2,total):
    result = Collatz(i)
    Collatz_dict[str(i)]=result
    if result > max[1]:
        max = [i,result]

print(max)
