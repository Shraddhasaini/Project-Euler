#Amicable numbers
#getting divisors
Amicable = []

def divisors(x):
    lstd=[1]
    for i in range(2,x):
        if x%i == 0:
            lstd.append(i)
    return sum(lstd)



def amicable():
    for i in range(1,10000):
        sumres = divisors(i)
        for j in range(i,10000):
            sumres1 = divisors(j)
            if (sumres == j) and (sumres1 == i):
                Amicable.append(sumres)
                Amicable.append(sumres1)
    return Amicable


print(amicable())
