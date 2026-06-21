#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The #program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a #Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the #dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

file = input('Enter the file name:')

counts = dict()
writer = None
bigcount = None

r_file = open(file,'r')
for line in r_file:
    a=line[0:5]
    if a =='From ' in line:
        
        emails = [line.split()[1]]
        for email in emails:
            counts[email] = counts.get(email,0) + 1

for email,count in counts.items():
    if writer is None or count > bigcount:
        writer = email
        bigcount = count

 
    if a !='From ' in line:
        continue

print(writer, bigcount)
