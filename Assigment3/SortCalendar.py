months = ['August', 'October', 'April','March','May','June']

from calendar import month_name
month_lookup=list(month_name)
res=sorted(months,key=month_lookup.index)
print(res)
