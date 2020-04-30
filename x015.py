n=[[1]*21]*21
#print n[0][1]
#print n[2][0]
k=21
for i in range(1,k):
    for j in range(1,k):
        n[i][j]=n[i-1][j]+n[i][j-1]
        #print 'n[',i,'][',j,'] = ',n[i][j]

print (n[20][20])
