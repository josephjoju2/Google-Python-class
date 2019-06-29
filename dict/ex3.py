import sys
d={'a':1,'b':5,'c':11,'d':7}
new=[]
for k,v in sorted(d.items()):
    if v>=5:
        new.append((k,v))
print(new)
for i in range(len(new)):
    print(new[i][1])


def myfcn(s): 
    return s[1]


new_list=sorted(new,key=myfcn)

d_new={}


for i in new_list:
    k=i[0]
    v=i[1]
    d_new[k]=v
print(d_new)
