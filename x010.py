import math
lst = [2]
for num in range(3,2000000,2):#O(N)
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1,2)):
        lst.append(num)

print(sum(lst))
