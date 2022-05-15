n=int(input("enter the number :"))
for i in range(1,n+1):
    print(" " * i, end="")
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()


for i in range(2,n+1):
    print(" " * (n+1 - i), end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()