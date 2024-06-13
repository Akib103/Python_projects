n=int(input())
room=0
for i in range(n):
    a,b=map(int,input().split())
    if a==b or b<a:
        room+=1
print(n-room)