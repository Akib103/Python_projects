n=str(input())
count=0
for i in range(0,len(n)):
    count=count
    if n[i]==str(4) or n[i]==str(7):
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")