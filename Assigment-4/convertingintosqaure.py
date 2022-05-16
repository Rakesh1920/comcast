n=int(input("Enter the number :"))
lst=[]

for i in range(n):
    lst.append(int(input("Enter the number:")))

for i in range(len(lst)):
    lst[i]=lst[i]*lst[i]

print(lst)