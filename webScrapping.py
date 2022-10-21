from bs4 import BeautifulSoup
import requests
from GetData import *
import pandas as pd
import re
def extract_url_details(url, count=0):
    content = []
    title2 = []
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36'}
    try:
        res = requests.get(url, headers=header, timeout=30)
    except:  
        return 
    if (res.status_code == 200):
        try:         
            soup = BeautifulSoup(res.content, "lxml")
            title = soup.title.string
            title2.append(title)
            meta = soup.find_all('meta')
            for tag in meta:
                if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description',                                                                                              'keywords']:                            content.append(tag.attrs['content'])
        except:
            content.append("no_details")
            title2.append("no_details")
    webScrap = [title2,content]
    if len(webScrap[1]) == 0:
        return None
    else: 
        return webScrap

url_dataSet = getUrls()
for x in url_dataSet:
    data = extract_url_details(x)
    if data != None:
        print(data)


