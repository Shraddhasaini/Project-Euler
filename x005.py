#Smallest Multiple
def multiple(x,y):
    c = 2520
    lst = []
    for i in range(x+1,y+1):
        if c % i == 0:
            lst.append(True)
        else: lst.append(False)
        print(lst)



print(multiple(1,10))
