#Define the number of rows for the triangle
n = 5
for i in range(n):                  #Loop for each row
    for j in range(i + 1):          #Loop for each coloumn in the present row   
        print("*", end="")          #Print * without a newline
    print()                         #Prints a newline at the end of each row

 
#Output: *
         **
         ***
         ****
         *****
