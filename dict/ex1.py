import os,pprint
os.chdir('/home/linux/pramod/python/google-python-exercises/basic')
f=open('alice.txt','r')
count_flag={}
new_list=[]

for line in f:
    new=line.split(' ')
    for i in new:
        new_list.append(i)
print(new_list)
    
    
for word in new_list:
    if word.lower() in count_flag:
        count_flag[word.lower()]+=1
    else:
        count_flag.setdefault(word.lower(),1)

pprint.pprint(count_flag)


f.close()

