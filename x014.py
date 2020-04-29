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
    dict = {}
    for i in range(1,1000000):
        x = len(collatz(i))
        dict.update({i : x} )
    return max(dict,key=dict.get)
print(number())
