import re

flog = open('test.txt', 'r')
fog = open('arg.txt', 'r')
 
flogLines = flog.readlines()
strlist=fog.readlines()

res = False
for line in flogLines:
    for fstr in strlist:    
        if re.search(fstr,line):
           print('found') 
           res = True
           break

           
if res:
    print('res true')
else: 
    print('res false')
    