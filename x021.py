#Amicable numbers
#getting divisors
amicable = []

def divisors(x):
    lstd=[1]
    for i in range(2,x):
        if x%i == 0:
            lstd.append(i)
    add = sum(lstd)


def amicable():



print(amicable())
