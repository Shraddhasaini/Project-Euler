file = open("f013.text", "r")
lst = []
for line in file.readlines():
    lst.append(int(line.strip()))
print(str(sum(lst))[:10])
