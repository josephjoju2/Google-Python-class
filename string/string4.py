def mixup(a,b):
    a1=a[0:2]
    b1=b[0:2]
    newa=b1+a[2:]
    newb=a1+b[2:]
    return(print(newa+' '+newb))

print('enter the string a')
a=str(input())
print('enter the string b')
b=str(input())
mixup(a,b)
