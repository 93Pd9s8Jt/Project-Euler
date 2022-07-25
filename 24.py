from itertools import permutations
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = [p for p in permutations(digits)]
print(sorted(perms)[1000000-1])
