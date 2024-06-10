'''n,h=map(int,input().split())
sum=0
for i in range(1,n+1):
    a=int(input())
    sum=sum
    if a<h or a==h:
        sum=sum+1
    elif a>h:
        sum=sum+2
print(sum)'''
n,h=map(int,input().split())
sum=0
height=list(map(int,input().split()))
for i in range(n):
    sum=sum
    if height[i]<=h:
        sum+=1
    else:
        sum+=2
print(sum)
    

