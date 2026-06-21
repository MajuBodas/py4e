#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the #file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

file = input('Open your file:')
r_file = open(file,'r')
#a = r_file.upper()

for line in r_file:
    line_ = line.upper().rstrip()
    print(line_)
