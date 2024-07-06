#Prompt the user to enter an input
a = input("Enter a string: ")

#Split the input string into a list of words
text = a.split()

#Initialize an empty string to build the acronym
x = ""

#Loop through each word in the list 'text'.
for i in text:
    x = x + i[0].upper()                  #Get the first character of each word, convert it to uppercase, and then append to 'x'
print(x)
