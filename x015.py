n=[[1]*21]*21
k=21
for i in range(1,k):
    for j in range(1,k):
        n[i][j]=n[i-1][j]+n[i][j-1]

print (n[20][20])
