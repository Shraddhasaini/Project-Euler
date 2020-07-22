def fac(x):
    mul = 1
    for i in range(2,x+1):
        mul = mul*i
    lst = []
    for i in range(0,len(str(mul))):
        lst.append(int(str(mul)[i]))
    print(sum(lst))

print(fac(100))
