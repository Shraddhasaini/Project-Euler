def collatz(n):
    lst = []
    while n > 1:
        lst.append(n)
        if (n % 2 == 0):
            n = n//2
        else:
            n = 3*n +1
    lst.append(1)
    return lst

def number():
    y = []
    for i in range(2,20):
        x = len(collatz(i))
        y.append(x)

print(number())
