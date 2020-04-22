#sum square
def sum_square(n):
    x = (n * (n+1) /2)**2
    y =  n*(n+1)*((2*n)+1)/6
    print("The sum of the squares of the first n natural numbers is",y)
    print("The square of the sum of the first n natural numbers is",x)
    return x - y


print("The difference is ",sum_square(10)) # 385,3025,2640
print("The difference is ",sum_square(100))

##shortter way
n=100
print((((n * (n+1) /2)**2)-(n*(n+1)*((2*n)+1)/6)))
