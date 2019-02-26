import re
flog = open('src.txt', 'r')
fog = open('arg.txt', 'r')

string = []
substr = []

for line in flog.readlines():
    string.append(line)
for line in fog.readlines():
    substr.append(line)
    
for st in string:
    for sub in substr:
        if :
            print("done")
        
if substr[5679] in string[0]:
    print("found")
    
s1 = '//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
s2 = '/pagead2'

if s2 in s1:
    print(s2)
    
def search():
    res = False
    for st in string:
        st = st[:-2]
        for sub in substr: 
            sub = sub[:-2]
            if sub in st:
                print('found') 
                res = True
                break
   
    if res:
        print('res true')
    else: 
        print('res false')
        

search()
