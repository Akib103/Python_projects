a,b,c=map(int,input().split())
borrow=0
for i in range(1,c+1):
    borrow=(borrow+(a*i))
    answer=borrow-b
if answer>0:
    print(answer)
else:
    print(0)