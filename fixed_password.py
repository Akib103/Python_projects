#fixed password
entry=(input())
password=entry.split()
pass_cor=1999
password=[int(i) for i in password ]
for i in password:
    if i==pass_cor:
        print("Correct")
        break
    else:
        print("Wrong")