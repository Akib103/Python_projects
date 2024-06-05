n=int(input())
b=input()
opinion=b.split()
opinion=[int(i) for i in opinion ]
count=0
for i in opinion:
    if i==1:
        print("HARD")
        break
    else:
        count=count+1
    if count==n:
        print("EASY")