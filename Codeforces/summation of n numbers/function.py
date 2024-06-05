#function
def sum(a):
    result=0
    for i in range(1,a+1):
        result=result+i 
    print(result)
n=int(input())
sum(n)