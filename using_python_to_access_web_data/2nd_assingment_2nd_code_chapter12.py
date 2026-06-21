# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = 0
count_ = 0
count_t = 0

# Retrieve all of the anchor tags
#exercício: passar todos os for & ifs pra função:

tags = soup('a')
for tag in tags:
    count = count + 1
    link = tag.get('href', None)
    
    if count == 3:
        print('count: ',count)
        print('Url: ',link)
        html = urllib.request.urlopen(url, context=ctx).read()
        link = tag.get('href', None)
        #print(html)
    
        for tag in tags:
            count_ = count_ + 1
            #link = tag.get('href', None)
            
            if count_ == 3:
                print('count: ',count_)
                print('Url: ',link)
                html = urllib.request.urlopen(url, context=ctx).read()
                link = tag.get('href', None)
                
                #for tag in tags:
                    #count_t = count_t + 1
                    #link = tag.get('href', None)
        
                    #if count_t == 3:
                        #print('count: ',count_t)
                        #print('Url: ',link)
                        #html = urllib.request.urlopen(url, context=ctx).read()
                        
                        #name = re.findall('^y(.)', link)
                        #name_ = name[0]
                        #print(name_)
                        
                        
                        
                         #^y_.
                        #    numbers = re.findall('[0-9]+',line_)
                       
