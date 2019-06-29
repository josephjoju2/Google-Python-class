def sort_last(x):
    new=[]
    alist=[]
    for i in x:
        a=i[-1]
        alist.append(a)
    alist.sort()
    for n in alist:
        for i in x:
            if n==i[-1]:
                new.append(i)
    return new
        
    
   

x=[(1, 7), (1, 3), (3, 4, 5), (2, 2)] 
print(sort_last(x))
