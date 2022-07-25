a = 1
b = 1
c = a+b
count = 3
while True:
    # a, b, c = Fx, Fx+1, Fx+2
    a = b+c
    b = a+c
    c = a+b
    count += 3 # count countains index of c
    if len(str(c)) == 1000:
        if len(str(b)) == 1000:
            if len(str(a)) == 1000:
                print(count-2)
            else:
                print(count-1)
        else:
            print(count)
        break
