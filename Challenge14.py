def is_leap(year):
    leap = False                                    #Initialize leap as False
     
    if (year%4==0) and (year%400==0):               #Check if the year is divisible by 4 and 400
        leap = True
       
    elif (year%4 == 0) and (year%100 != 0):         #Check if the year is divisible by 4 but not by 100
        leap = False
    return leap

year = int(input())                                 #Prompt the user to enter an input 
print(is_leap(year))                                #Print whether the year is a leap year or not
