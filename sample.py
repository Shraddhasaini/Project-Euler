hypo = lambda a,b,c : a if (max(a,b,c)==a) else (b if (max(a,b,c)==b) else c)
print(hypo(3,4,5))
