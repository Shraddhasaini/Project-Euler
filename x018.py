file = open("f018.text", "r")
lst = []
for line in file.readlines():
    text = line.split()
    print(text)
