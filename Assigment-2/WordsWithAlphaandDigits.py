s=input("Enter the String :")
l=s.split(" ")
for i in l:
    if i.isalnum() and not i.isalpha() and not i.isdigit():
        print(i)