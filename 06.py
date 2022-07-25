total = 0
squares = 0
for i in range (1, 101):
    total += i
    squares += i**2
    print(i)
print(0)
total_square = total ** 2
diff = total_square - squares
print(diff)
