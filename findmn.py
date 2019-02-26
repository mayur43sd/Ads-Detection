import requests
from bs4 import BeautifulSoup as bs

def find_main(self):
       source = requests.get(url, timeout=1000)
        plaintext = source.text
        soup = bs(plaintext)
  
        fw = open('sites.txt','w')
        links = soup.findAll('div', {'class':'DescriptionCell'})
        for link in links:    
            if link != None:
                fw.write(link.a.text)
                fw.write('\n')
        fw.close()
  