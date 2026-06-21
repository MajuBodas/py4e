#testing_course_5.py

import csv

#import sqlite3

#conn = sqlite3.connect('content.sqlite')
#cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS Baby_names')

#cur.execute('''CREATE TABLE IF NOT EXISTS Baby_names
 #   ( year_of_birth INTEGER, gender TEXT, ethnicity TEXT,
 #    Childs_first_name TEXT, count INTEGER, rank INTEGER)''')

#count = 0
#counts = dict()
#years = dict()

file = 'Popular_Baby_Names.csv'

with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    genders = []
    for row in reader:
        gender = row[1]
        genders.append(gender)
        
print(genders)

    
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)
    
    #print(header_row)
    
    

#r_file = open(file,'r')


#for line in r_file:
#    line_ = line.split(',')
#    years = (line_[0])
    #print(years)
    
#type(years)

    
    
    #for year in counts:
        #if year in counts:
            #counts[year] = 1
        #else:
            #counts[year] = counts[year] + 1
#print(counts)
            
   
    
    #print(years)

    #for year in years: 
#    if year in counts:
#        counts[year] = counts[year] + 1
#    else:
#        counts[year] = 1
#print(counts)
        
        #counts[year] = counts.get(year,0) + 1
        #print(counts[year])   
        
        #emails = [line.split()[1]]
        
        
        #if year not in counts:
            #counts[year] = 1
        #else:
            #counts[year] = counts[year] + counts[year]

    
    #count = count + 1
    #dict_year[line_] = dict_year.get(line_, 0) + 1
    #counts[tuple_year] = counts.get(tuple_year, 0) + 1
    #dict_year[line_] = dict_year.get(line_, 0) + 1
        
        #year = line_[0]
        #gender = line_[1]
        #etnia = line_[2]
        #name = line_[3]
        #name_qtd = line_[4]
    #count = count + 1
        

#print(years)        
#print(counts[year])   

#print(counts[tuple_year])
#print(line_)
#print(year)
#print(gender)
#print(etnia)
#print(name)
#print(name_qtd)

#print(dict_year[year])

#print('Qtd de linhas:',count)

    
    
#conn = sqlite3.connect('content.sqlite')
#cur = conn.cursor()

#baseurl = "https://data.cityofnewyork.us/Health/Popular-Baby-Names/25th-nujf/data_preview"



