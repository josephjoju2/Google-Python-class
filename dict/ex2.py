import os,pprint,sys
os.chdir('/home/linux/pramod/python/google-python-exercises/basic')
f=open('alice.txt','r')
count_flag={}
new_list=[]

for line in f:
    new=line.split(' ')
    for i in new:
        new_list.append(i)
#print(new_list)
    
    
for word in new_list:
    if word.lower() in count_flag:
        count_flag[word.lower()]+=1
    else:
        count_flag.setdefault(word.lower(),1)


top=[]
for k,v in count_flag.items():
    if v>=55:
        top.append((k,v))

def myfcn(s):
    return s[1]

new_list=sorted(top,key=myfcn)

p=new_list.index(new_list[-20])

d_new=[]
for i in range(p,len(new_list)):
    d_new.append(new_list[i])

mm=[]    
for i in range(1,len(d_new)):
    mm.append(d_new[-i])

#print(new_list)

#print(d_new)

pprint.pprint(mm)






f.close()

