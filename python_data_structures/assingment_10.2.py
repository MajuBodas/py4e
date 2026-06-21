#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then #splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file = input('Enter the file name:')
file_ = open(file,'r')


counts = dict()
lst = list()
hr=0

for line in file_:
    text_ = line.rstrip()
    #count = count + 1
    #print(text_)
    
    a=line[0:5]
    if a =='From ' in line:
        b = line.split()
        c = (b[5])
        hrs = c.split(':')[0:1]
        #print(hrs)
        for hr in hrs:
            counts[hr] = counts.get(hr,0) + 1
             
       # print(counts[hr])
        
for key, val in counts.items():
    newtup = (key,val)
    lst.append(newtup)
   
        
lst = sorted(lst, reverse=False)
for key, val in lst[:27]:
    print(key,val)
