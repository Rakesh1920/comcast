count=0
for i in range(50,150):
    flag = False
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                flag = True
                break
    if flag==False:
        count+=1
print(count)