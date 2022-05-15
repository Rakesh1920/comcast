s=input("Enter the string :")
letters=0
digits=0
specialChar=0
for i in range(0,len(s)):
    if s[i].isalpha():
        letters=letters+1
    elif s[i].isdigit():
        digits=digits+1
    else:
        specialChar=specialChar+1
print(f"count of letters : {letters}")
print(f"Count of digits : {digits}")
print(f"count of specialCharacters : {specialChar}")