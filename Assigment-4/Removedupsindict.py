d1={1:'rakesh',2:'ramesh',3:'suresh',4:'rakesh',5:'lokesh',6:'ramesh'}
temp=[]
res={}
for k,v in d1.items():
    if v not in temp:
        temp.append(v)
        res[k]=v
print(res)
