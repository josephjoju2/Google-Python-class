def front_back(a,b):
    if len(a)%2==0:
        x=int(len(a)/2)
       
    else:
        x=int((len(b)/2)+1)
        
    if len(b)%2==0:
        y=int(len(b)/2)
   
    else:
        y=int((len(b)/2)+1)

    fronta=a[:x]
    backa=a[x:]  
    frontb=b[:y]
    backb=b[y:]

    return(fronta+frontb+backa+backb)

print(front_back('abcd','xyz'))
   
