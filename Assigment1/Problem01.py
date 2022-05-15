a=0
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i):
        a=a+1
        print(a,end="")
    print()