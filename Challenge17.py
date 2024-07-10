#Prompt the user to enter a number
n = int(input("Enter a number:"))

#Initialize sum to 0 (This will store the sum of the cubes of each digits)
sum = 0

#Convert the number to a string and find its length
n1 = len(str(n))

#Store the original number, n in a temporary variable
temp = n

while temp>0:
    rem = temp%10                             #To get the last digit of the temporary number
    sum += rem **n1                           #Add the digit raised to the power of the number of digits of n1 to 'sum'
    temp//= 10                                #Remove the last digit from the temp

#After the loop, check if the original number is equal to the calculated sum
if n==sum:
    print(n, "YES")
    
else:
    print(n,"NOOOO!")
