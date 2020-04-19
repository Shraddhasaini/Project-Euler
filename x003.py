import math
lst = []
def primefactor(n):
    for i in range(2,math.ceil(math.sqrt(n))):
        if ( n % i == 0 ):
            #print(i)
            lst.append(i)
            n = n/i
    return max(lst)

print(primefactor(600851475143))
