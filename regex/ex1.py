import re, sys, os
year_name_rank=[]
baby_list=[]
def baby_names(filename):
    f=open(filename,'rU')
    text=f.read()


    year_match=re.search(r'Popularity\sin\s(\d\d\d\d)',text)
    year=year_match.group(1)
    
    baby_list.append(year)
    
    tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text)
    rank_name={}
    for (rank,boy_name,girl_name) in tuples:
        if boy_name not in rank_name:
            rank_name[boy_name]=rank
        if girl_name not in rank_name:
            rank_name[girl_name]=rank
    sorted_names=sorted(rank_name.keys())
    
    for name in sorted_names:
        baby_list.append(name+' '+rank_name[name]) 
    print(baby_list)   
            
    

    f.close()

filename='baby1990.html' 
baby_names(filename) 
 
