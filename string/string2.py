def both_ends(s):
    if len(s)<=2:
        return(print('there should be enouf length for str'))


    else:
        new_string=s[0:2]+s[-2:]
        return print(new_string)

print('enter the string')
s=str(input())
both_ends(s)
