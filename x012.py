from sympy import *

def trinumbers():
    for i in range(1000,10000000000):
        x = int(i*(i+1)/2)
        if (len(divisors(x)) > 500):
            return x


print(trinumbers())
