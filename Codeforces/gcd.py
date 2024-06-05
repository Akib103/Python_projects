#GCD
a,b=map(int,input().split())
if a==0 or b==0:
    print(1)
elif a>b:
    small=b
    big=a
elif a<b:
    small=a
    big=b
else: 
    print(a)
i=small
while i>=1:
    if big%i==0 and small%i==0:
        print(i)
        break
    i=i-1