#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
"""
Client per a la web https://www.packtpub.com/packt/offers/free-learning/
"""
class Client(object):
    def get_web(self,page):
        """ baixar-se la web  """
        f=urllib2.urlopen(page)
        html=f.read()
        f.close()
        return html
    def search_text(self,html):
        """Buscar text"""
        soup=BeautifulSoup(html,'html.parser')
        title=soup.find("div","dotd-title")
        print title.text



    def main(self):
        web=client.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        client.search_text(web)





if __name__ == "__main__":
    client=Client()
    client.main()
