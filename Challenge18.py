#Function to check if two strings are anagrams or not
def check_anagram(a1,a2):
    if(sorted(a1) == sorted(a2)):                               #The sorted strings are checked
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         
a1 = "angel"
a2 = "glean"
check_anagram(a1, a2)
