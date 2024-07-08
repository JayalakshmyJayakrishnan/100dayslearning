def is_leap(year):
    #Initialize leap as False
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        #If divisible by 4, check if it's also divisible by 100
        if year % 100 == 0:
            #If divisible by 100, check if it's also divisible by 400
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    
    return leap

#Read an integer input representing the year from the user
year = int(input("Enter a year: "))
#Print whether the year is a leap year or not
print(is_leap(year))
