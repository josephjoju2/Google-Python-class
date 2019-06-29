import os
directory='/home/linux/pramod/python'
filenames=os.listdir('/home/linux/pramod/python')
for elem in filenames:
    try:
        path=os.path.join(directory,elem)
        print(elem)
        print(os.listdir(path))
    except:
        print('something is wrong')

print(os.path.abspath('.'))


