#calculator_basic operations
a,b,c=map(str,input().split())
d=int(a)
e=int(c)
if b=="+":
    result=d+e
elif b=="-":
    result=d-e
elif b=="*":
    result=d*e
elif b=="/":
    result=d/e
print(result)