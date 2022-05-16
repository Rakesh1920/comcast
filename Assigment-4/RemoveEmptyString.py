lst=['carrot','','tomato','','apple','grapes','']

for l in lst:
    if len(l)==0:
        lst.remove(l)
print(lst)