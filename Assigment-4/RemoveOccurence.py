lst=['grapes','apples','oranges','mangoes','apples','pineapple','lemon','apples','apples']
x='apples'
for l in lst:
    if lst.count(x)!=0:
        lst.remove(x)
print(lst)