import urllib.request as ur_ 
import json




url = input("Enter URL:")

print('Retrieving URL', url)

# http://py4e-data.dr-chuck.net/comments_42.json


sum = 0


data = ur_.urlopen(url).read()
info = json.loads(data)



for item in info["comments"]:
    count_ = int(item["count"])
    sum = sum + count_
    
print(sum)
    
    
    
  