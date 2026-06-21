#testando o try except 

age = input('What is your age?')

try:
    new_age = int(age)
   
except:
    new_age = age
    #print('unfortunately you did not input the age in numbers, I am sorry, you will be able to try again')
    
#print('end of code',new_age)
if type(new_age) == int:
    snd_new_age = new_age + 10
    print('In 10 years you will be:',snd_new_age) 
if type(new_age) != int:
    print('unfortunately you did not input the age in numbers, I am sorry, you will be able to try again, just call the file')
    
    
   
        