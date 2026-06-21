import urllib.request as ur, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter Url:')

total_number = 0
sum = 0 

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)

counts = tree.findall('.//count')


for i in counts:
    sum = sum + int(i.text)
    total_number = total_number + 1
    
    
print(sum)