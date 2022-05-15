s=input("Enter the string :")
n=int(input("Enter the index number :"))
res=''
for i in range(0,len(s)):
    if(i!=n):
        res=res+s[i]
print(res)