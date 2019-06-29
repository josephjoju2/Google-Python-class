def verbing(s):
    
    if s.endswith('ing'):
        newstring=s[:-3]+'ly'
        return(newstring) 
    else:
        newstring=s+'ing' 
        return(newstring)

print('enter the string')
s=str(input())
if len(s)>=3:
   print(verbing(s))
else:
   print('the string anit long enouf')   

