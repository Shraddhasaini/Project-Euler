
def Triplet(n):#O(N^2)
    for a in range(1, 400):
        for b in range(1, 400):
            c = (n - a) - b
            hypo = lambda a,b,c : a if (max(a,b,c)==a) else (b if (max(a,b,c)==b) else c)
            al = lambda a,b,c : b if (max(a,b,c)==a) else (c if (max(a,b,c)==b) else a)
            base = lambda a,b,c : c if (max(a,b,c)==a) else (a if (max(a,b,c)==b) else b)
            if (hypo(a,b,c)**2 == al(a,b,c)**2 + base(a,b,c)**2):
                print("Hypotenuse is:", hypo(a,b,c))
                print("Altitude is:", al(a,b,c))
                print("Base is:", base(a,b,c))
                return hypo(a,b,c)*al(a,b,c)*base(a,b,c)


print(Triplet(1000))
