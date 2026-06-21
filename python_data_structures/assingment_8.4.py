#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() #method. The program should build a list of words. For each word on each line check to see if the word is already in the list and #if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in #the desired output.


file = input('Enter the file name:')

r_file = open(file,'r')
word = list()
words_list = list()

for l in r_file:
    lines = l.split()
    for i in range(len(lines)):
        word = lines[i]
        if not word in words_list:
            words_list.append(word)
        if word in words_list:
            continue
words_list.sort()
print(words_list)
