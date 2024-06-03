#bear and big brothers
a,b=map(int,input().split())
bear=a
brother=b
for i in range(1,(a*b)+1):
    bear=bear*3
    brother=brother*2
    if bear>brother:
        print(i)
        break
