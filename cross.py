import re
import pandas as pd

#Cross-Referencing with EasyList
flog = open('output.txt', 'r')
fog = open('arg.txt', 'r')

string = []
substr = []

for line in flog.readlines():
    string.append(line)
for line in fog.readlines():
    substr.append(line)

ad = []

def search():
    
    res = False
    for st in string:
        st = st[:-2]
        for sub in substr: 
            sub = sub[:-2]
            if sub in st:
                res = True
                break
            else:
                res = False
                
        if res:
            ad.append("ad")
        else:
            ad.append("non-ad")
    
    return ad

search()        

#Creatinf Dataset
def create_ds():
    records = []
    fr = open('output.txt','r')
    for line in fr.readlines():
        line = line[:-2]
        length = len(line)
        special_char = re.findall('[!@#$%^&*(),.?":{}|<>]', str(line))
        
        records.append((line,length,special_char))
    
        
    df = pd.DataFrame(records, columns=['URL','Length-of-url','Special_chars'])
    df['Ads_Class'] = ad
    df.to_csv('temp_dataset.csv',index=False,encoding='utf-8')
 
    
create_ds()