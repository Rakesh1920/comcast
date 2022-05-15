s=input("Enter the String :")
lRes=''
URes=''
for i in range(0,len(s)):
    if s[i].islower():
        lRes=lRes+s[i]

for i in range(0,len(s)):
    if s[i].isupper():
        URes=URes+s[i]
res=lRes+URes
print(res)
