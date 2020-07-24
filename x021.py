#Amicable numbers
import math
list=[0]*10001
def nod(n):
    count=0
    sum=-n
    m=math.sqrt(n)
    i=1
    while i<m:
        if n%i==0:
            sum+=i+(n/i)
        i+=1

    if int(m)==m:
        sum+=m
    if n==1:sum=1
    return int(sum)


n=10000
i=0
sum=0
while i<n:
    if list[i]!=0:
        x=nod(i)
        if x==list[i]:
            sum+=list[i]+i
    else:
        x=nod(i)
        if x!=1 and x<10000:
            list[x]=i
    i+=1
print sum
