                                                          _#Prompt the user to enter an input_
year = int(input("Enter an year: "))



if (year%400 ==0) and (year%100 == 0):                    _#Check if the input is divisible by both 400 and 100, then it's a leap year_
    print("{} is a leap year".format(year))
elif (year%4 == 0) and (year%100 != 0):                   _#Check if the input is divisible by 4 but not by 100, then it's a leap year_
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))           _#If the above conditions are not satisfied, then it's not a leap year_
