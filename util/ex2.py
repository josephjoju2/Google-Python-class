import os
directory=os.path.basename('..')
filenames=os.listdir(directory)
for filename in filenames:
    print (os.path.join(directory,filename)) 
    print(os.path.abspath(os.path.join(directory,filename)))
