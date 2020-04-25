

def Triplet(n):
    hypo = lambda a,b,c : a if (max(a,b,c)==a) else (b if (max(a,b,c)==b) else c)
    al = lambda a,b,c : b if (max(a,b,c)==a) else (c if (max(a,b,c)==b) else a)
    base = lambda a,b,c : c if (max(a,b,c)==a) else (a if (max(a,b,c)==b) else b)
    x = hypo(a,b,c)**2
    y = al(a,b,c)**2
    z = base(a,b,c)**2
    if (x == y +z):
        




        return hypo(a,b,c)*al(a,b,c)*base(a,b,c)


print(Triplet(1000))
