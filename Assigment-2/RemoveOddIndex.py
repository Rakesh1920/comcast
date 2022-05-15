s=input("Enter the string:")
res=''

for i in range(0,len(s)):
    if i%2==0:
        res=res+s[i]
print(res)

