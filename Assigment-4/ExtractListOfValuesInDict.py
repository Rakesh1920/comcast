d1=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
d2=[]

for l in d1:
    for k in l.keys():
        if k=='Science':
            d2.append(l[k])
print(d2)

d3=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
d4=[]

for l in d1:
    for k in l.keys():
        if k=='Math':
            d4.append(l[k])
print(d4)
