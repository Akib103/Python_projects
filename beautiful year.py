#beautiful years:
n=int(input())
for i in range(1,100001):
    a=n+i
    b=str(a)
    if b[0]!=b[1] and b[1]!=b[2] and b[2]!=b[3] and b[0]!=b[2] and b[0]!=b[3] and b[1]!=b[3] :
        print(int(a))
        break
