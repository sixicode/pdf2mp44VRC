import requests
import re
import json
from bs4 import BeautifulSoup as bs

class downloader():
    def __init__(self):
        pass
    
    def get_sci_hub_url(self):
        url='https://lovescihub.wordpress.com/'
        res=requests.get(url)
        soup = bs(res.text, "html.parser")
        selector='#post-22 > div > p:nth-child(2) > a'
        elements = soup.select(selector)
        # for element in elements:
        #     print(element.attrs['href'])
        return elements[0].attrs['href']

    def get_url(self, doi):
        return self.get_sci_hub_url()+'/'+doi

    def pdf_downloader(self):
        pass

dlr=downloader()
print(dlr.get_url('10.1126/science.1186799'))

