def match_ends(l):
    count=0
    for i in l:
        if (len(i)>=2) and (i[0]==i[-1]):
            count+=1
    return count

l=['cat','f','d','non','dod']
print(match_ends(l))
