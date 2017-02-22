#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import urllib2
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
    



if __name__ == "__main__":
    client=Client()
    web=client.get_web("https://www.packtpub.com/packt/offers/free-learning/")
    print web
