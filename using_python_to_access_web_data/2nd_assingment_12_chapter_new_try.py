# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')



html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = 0
count_ = 0

# Retrieve all of the anchor tags

#Step 1: write the import lines and the user prompts for url/count/position. Do not hard code any values.

tags = soup('a')
for tag in tags:    
    count = count + 1
   
    if count == 3:
        print(tag.get('href', None))
        url = input(tag.get('href', None))
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        
        tags = soup('a')
        for tag in tags:    
            count_ = count_ + 1
            if count_ == 3:
                print(tag.get('href', None))
        
        
        
        #new_url = input(tag.get('href', None))
        #html = urllib.request.urlopen(new_url, context=ctx).read()
        #new_tags = soup('a')
        #print(new_tags)
        
       
                