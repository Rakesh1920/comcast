lst1=[1,2,3]
lst2=['java','python','php']
dit={}
for i in lst1:
    for j in lst2:
        dit[i]=j
        lst2.remove(j)
        break
print(dit)