#testing_15.py

# C:\Users\bodas\Documents\py4e\code3\mbox.txt

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    org_pieces = line.split('@')
    org = org_pieces[1]

    
    print(org)
    
    
