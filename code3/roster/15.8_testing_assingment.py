# 15.8_testing_assingment.py

#15.8_assingment.py  C:\Users\bodas\Documents\py4e\code3\roster

#"C:\Users\bodas\Downloads\roster_data.json"

#C:/Users/bodas/Downloads/roster_data.json
import json

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))