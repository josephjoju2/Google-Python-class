def linear_merge(list1,list2):
    newlist=list1+list2
    newlist.sort()
    return newlist
print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
