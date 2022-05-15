import math

num=int(input("Enter the number:"))
a=num
res=0
while num>0:
    temp=num%10;
    res=res+math.factorial(temp)
    num=int(num/10)

if res==a:
    print("YES")
else:
    print("NO")