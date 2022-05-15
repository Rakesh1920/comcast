s=input("Enter the string :")
l=s.split(" ")
t=[]
for i in l:
    if i not in t:
        print(l.count(i))
        t.append(i)