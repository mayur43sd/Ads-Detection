import re
import requests
from bs4 import BeautifulSoup


page_link = 'https://www.geeksforgeeks.org/'

sourcecode = requests.get(page_link)
#page_response = requests.get(page_link, timeout=5)
page=sourcecode.text

#page_content = BeautifulSoup(page_response.content,'html.parser')
soup = BeautifulSoup(page,"lxml")
with open("f1.txt","w") as out_file:
 for sources in soup.findAll('a'):
  href = sources.get('href')
  out_file.write(href)
  stri = "\n"
  out_file.write(stri)
 # print(href)i
 for links in soup.findAll('script'):
     
    jsc = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',str(links))
    print(jsc)
    # stri = "\n"
    #out_file.write(stri)



#urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url) 