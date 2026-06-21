#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the #hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to #test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. #Do not worry about error checking the user input - assume the user types numbers properly.


hrs = input('Enter hours:')
rate = input('Rate per hour:')

new_hrs = float(hrs)
new_rate = float(rate)

if new_hrs <= 40:
    pay = new_hrs*new_rate
    print(str(pay),'gross pay when hours <=40')
    
if new_hrs > 40:
    pay = 1.5*new_rate*(new_hrs-40)+40*new_rate
    print(str(pay),'gross pay when hours > 40')
    
print('end of code')
    
    