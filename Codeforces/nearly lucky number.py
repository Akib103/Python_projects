n=str(input())
count=0
for i in range(0,len(n)):
    count=count
    if n[i]==str(4) or n[i]==str(7):
        count+=1
if int(n)==4 or int(n)==7:
    print("YES")
elif count==len(n):
    print("YES")
else:
    print("NO")