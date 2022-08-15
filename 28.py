spiral = 1001
num = 1
nums = [1]
for i in range(2, spiral, 2):
    nums.append(4*num + 10*i)
    num += 4*i 
print(sum(nums))
