num = 600851475143
i=2
while num != 1:
    if num % i == 0 :
        if num / i == 1:
            print(i)
            break
        num /= i
    i+=1
