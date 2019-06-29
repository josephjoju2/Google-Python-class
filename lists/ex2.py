def front_x(l):
    list1=[]
    list2=[]
    for i in l:
        if i[0]=='x':
            list1.append(i)
        else:
            list2.append(i)
    list1.sort()
    list2.sort()
    newlist=list1+list2 
    return newlist

l=['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
print(front_x(l))
         
