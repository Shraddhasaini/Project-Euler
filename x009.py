
def hypo(a,b,c):
    h = 0
    if (max(a,b,c)==a):
        h = a
        al = b
        base = c
    elif (max(a,b,c)==b):
        h = b
        al = a
        base = c
    else:
        h = c
        al = a
        base = b
    return h, al, base

print(hypo(1,2,3))
