 #Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate #for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the #computation of pay in a function called computepay() and use the function to do the computation. The function should return a #value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a #string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you #can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
    

a = input('Hours:')
b = input('Rate per hour:')
    
def computepay(a,b):

    new_hrs = float(a)
    new_rate = float(b)
    
    if new_hrs<=40:
        pay=new_hrs*new_rate
        
    else:
        pay = 40*new_rate+(new_hrs-40)*new_rate*1.5

    
    return(pay)
    
print('Pay',computepay(a,b))