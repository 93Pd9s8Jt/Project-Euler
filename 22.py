with open("p022_names.txt", 'r') as file:
    exec("names = ["+file.read()+"]")

names.sort()
total = 0
for index, name in enumerate(names):
    nametotal = 0
    for char in name:
        nametotal += ord(char) - ord("A") + 1
    total += nametotal*(index+1)
print(total)
