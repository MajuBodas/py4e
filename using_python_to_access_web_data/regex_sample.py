import re

#file = input('')
#file_ = open(file,'r')

sum_n_ = 0

file = open('regex_sum_1971580_actual_data.txt','r')
for line in file:
    line_ = line.rstrip()
    numbers = re.findall('[0-9]+',line_)
    if numbers != []:
        for element in numbers:
            n_ = int(element)
            sum_n_ = sum_n_ + n_
print(sum_n_)


        #number_ = int(numbers)
        #sum_numbers = sum_numbers + number_
        #print(sum_numbers)
    
    #print(line_)
    
    
    
    
    
    
    #number = re.findall((,line_))


# text = "X-DSPAM-Confidence:    0.8475"


# a = text.find('5')
# e = text.find('0')



#file = input('Enter the file name:')

#r_file = open(file,'r')
#word = list()
#words_list = list()

#for l in r_file:
#    lines = l.split()
#    for i in range(len(lines)):
#        word = lines[i]