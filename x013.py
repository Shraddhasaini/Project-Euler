file = open("f013.text", "r")
lst = []
Lines = file.readlines()
count = 0
# Strips the newline character
for line in Lines:
    lst.append(int(line.strip()))
x = sum(lst)
