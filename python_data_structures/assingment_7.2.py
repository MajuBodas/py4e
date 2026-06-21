#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and #produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as #the file name.


file = input("Please, enter the file name: ")
i = 0
c = 0

try:    
    r_file = open(file,'r')
    for line in r_file:        
        if not 'X-DSPAM-Confidence:' in line:
            continue
        if 'X-DSPAM-Confidence:' in line:
            # input in her we how iill select the complete line that starts with data X-DSPAM-Confidence: 
            #for i in line 
            i = i+1
            a = line[21:27]
            b = float(a)
            #print(b)
            c = c+b 
    d=c/i
    #print('There were ',i,' lines within the format X-DSPAM-Confidence followed by a decimal number')
    #print('Summing up all the decimal elements in the desired format, there is a total of:',c)
    print('Average spam confidence:',d)

except:
    print('File cannot be opened ',file)
    quit()


    #a = line.rstrip()
    #print(a)
    #desire_line = 
    #text.txt.txt
