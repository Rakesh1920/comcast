lst=[2,3,1,6,4,5]

largestNumber=0
secondLargest=0
smallestNumber=lst[0]
secondSmallest=lst[0]
for i in range(len(lst)):
    if lst[i]>largestNumber:
        largestNumber=lst[i]
print(f"The largest number in the list is :{largestNumber} ")

for i in range(len(lst)):
    if lst[i]>secondLargest and lst[i]<largestNumber:
        secondLargest=lst[i]
print(f"The secondlargest number in the list is :{secondLargest} ")



for i in range(1,len(lst)):
    if lst[i]<smallestNumber:
        smallestNumber=lst[i]
print(f"The smallest number in the list is :{smallestNumber} ")

for i in range(1,len(lst)):
    if lst[i]<secondSmallest and lst[i]>smallestNumber:
        secondSmallest=lst[i]
print(f"The secondsmallest number in the list is :{secondSmallest} ")



