def findSmallestMultiple(n):
    for i in range(n, factorial(n) + 1, n):
        if isMultiple(i, n):
            return i
    return -1

def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1

print (findSmallestMultiple(10)) # 2520
print (findSmallestMultiple(20))
