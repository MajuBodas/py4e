import json
import urllib.request as UR


url = input('Enter location: ')

count = 0

print('Retrieving', url)
xml = UR.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

info = json.loads(xml)

print(info)