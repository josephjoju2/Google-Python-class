def fcn(a):
    return a[-1]
    
def sort_last(tuples):
    new=sorted(tuples,key=fcn)
    return new
tuples=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sort_last(tuples))

    
