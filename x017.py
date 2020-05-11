def f(n):
    if n==1:return 3
    if n==2:return 3
    if n==3:return 5
    if n==4:return 4
    if n==5:return 4
    if n==6:return 3
    if n==7:return 5
    if n==8:return 5
    if n==9:return 4
    if n==10:return 3
    if n==11:return 6#eleven
    if n==12:return 6#twelve
    if n==13:return 8#thirteen
    if n==14:return 8#fourteen
    if n==15:return 7#fifteen
    if n==16:return 7#sixteen
    if n==17:return 9#seventeen
    if n==18:return 8#eighteen
    if n==19:return 8#nineteen
    if n==20:return 6#twenty
    if n==30:return 6#thirty
    if n==40:return 6#fourty
    if n==50:return 5#fifty
    if n==60:return 5#sixty
    if n==70:return 7#seventy
    if n==80:return 6#eighty
    if n==90:return 5#ninty
    if n==100:return 10#hundred

def f1(i,sum):
    if i<=20 or i==30 or i==40 or i==50 or i==60 or i==70 or i==80 or i==90 or i==100:
        x=f(i)
        sum+=x
    elif i>20 and i<=99:
        j=(i/10)*10
        k=i%10
        sum=sum+f(j)+f(k)
    return sum
def f2(i):
    sum=0
    if i<=20 or i==30 or i==40 or i==50 or i==60 or i==70 or i==80 or i==90 or i==100:
        x=f(i)
        sum+=x
    elif i>20 and i<=99:
        j=(i/10)*10
        k=i%10
        sum=sum+f(j)+f(k)
    return sum

n=1
sum=0
for i in range(1,101):
    sum=f1(i,sum)

y=(sum-10)*10
z=y
print(sum)
for i in range(101,1000):
    sum+=10 #for every 'hundred and'
    if i%100!=0:
        x=i%100
        sum=sum+3+f2(x)

sum=sum+200+100+100+200+200+100+11
print(sum)
y=y+8980+300+300+500+400+400+300+500+500+400+11
print(y)
z=z+8910+300+300+500+400+400+300+500+500+400+11+63
print(z)
