n=int(input())

for i in range(1,n+1):
    a,b=map(int,input().split())
    sum=0
    for t in range(a,b+1):
        sum=sum+t
    print(sum)