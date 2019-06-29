def not_bad(s):
    n=s.index('not')
    b=s.index('bad')
    if n<b:
        edited=s[:n]
        newstring=edited+'good'
        return(newstring)
    else:
        return(s)
print('enter a string')
s=str(input())
print(not_bad(s))
