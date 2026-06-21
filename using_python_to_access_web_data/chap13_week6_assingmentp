import urllib.request as ur_ #, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl

import json

url = input("Enter URL:")

print('Retrieving URL', url)

# http://py4e-data.dr-chuck.net/comments_42.json


sum = 0



data = ur_.urlopen(url).read()

info = json.loads(data)

count = info.findall('count:')

#print('User count:', len(info))

#print(info)

for item in count:
    print("name:",item["name"])
    print('count:',item['count'])
    
    
    #sum = sum + comment["count"]
    
#print(sum)