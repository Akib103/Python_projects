#wrong substraction
n,k=map(int, input().split())
for i in range(1,k+1):
    if n%10!=0:
        result=n-1
        n=result
    else:
        result=n//10
        n=result
print(result)