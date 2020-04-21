#Smallest Multiple
def multiple(x,y):
    c = 2
    lst = [True]
    for i in range(x+1,y+1):
        for j in lst:
            if (j == True):
                if c % i == 0:
                    lst.append(True)
                else: lst.append(False)
            else:
                c += 1
    print(lst)
    print(str(c))




print(multiple(1,3))
