def fix_start(s):
    if len(s)>1:
        f=s[0]
        string=s[1:]
        s=string.replace(f,'*')
        n=f+s
        return(print(n))
    else:
        return(print('not enuf length for str'))


print('enter the string')
s=str(input())
fix_start(s)
