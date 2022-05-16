#d1={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d1={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
d2={}

for k in d1.keys():
    d2[d1[k]]= len(str(d1[k]))
print(d2)