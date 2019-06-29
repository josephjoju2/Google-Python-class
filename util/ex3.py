import os, sys, commands
print(os.listdir('/home/linux/pramod'))
cmd='ls -l '+ '/home/linux/pramod'
(status,output)=commands.getstatusoutput(cmd)
if status:
    sys.stderr.write(output)
    sys.exit(status)
print(output)
