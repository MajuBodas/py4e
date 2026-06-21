 #Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print #out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except #and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
    
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        
    try:
        new_num = float(num)
    except:
        print('Invalid input')
        continue
    
    if smallest is None:
        smallest = new_num
    elif smallest > new_num:
        smallest = new_num
        
    if largest is None:
        largest = new_num
    elif largest < new_num:
        largest = new_num

print("Maximum",largest)

print("Minimum",smallest)

print('End of the Code')



