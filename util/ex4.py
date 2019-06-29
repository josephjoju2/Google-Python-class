import os,sys
filenames=os.listdir('.')
for filename in filenames:
    try:
        f=open(filename,'rU')
        text=f.read()
        print(filename+'\n'+text)
        f.close()
    except IOError:
        sys.stderr.write('problem reading '+filename+'\n')

