
def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

def even(seq):
    for number in seq:
        if not number % 2:
            yield number

def under_a_million(seq):
    for number in seq:
        if number > 4000000:
            break
        yield number

res= sum(even(under_a_million(fib())))
print(res)
