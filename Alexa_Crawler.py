class crawl:
    def imp(self):
        import requests
        from bs4 import BeautifulSoup as bs
    
    def init(self, url): 
        url = "http://" + url
        source = requests.get(url, timeout=1000)
        plaintext = source.text
        soup = bs(plaintext)
   
    def find_main(self):
        fw = open('sites.txt','w')
        links = soup.findAll('div', {'class':'DescriptionCell'})
        for link in links:    
            if link != None:
                fw.write(link.a.text)
                fw.write('\n')
        fw.close()
    
    def iterate(self):
        fr = open('sites.txt','r')
        fw = open('output.txt','w')
        for line in fr.readlines():
            self.init(line)
            for link in soup.findAll('script'):
                href = link.get('src')
                if href != None:
                    fw.write(href)
                    fw.write('\n')
        fw.close()
        fr.close()
       
    def main(self):
        self.imp()
        self.iterate()
      
        
c = crawl()   

c.main()