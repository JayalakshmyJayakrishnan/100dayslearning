def rem_occ(lst,num):
    return [x for x in lst if x!= num]
    
lst = map(int, input("Enter a list of numbers(space-separated): ").split())
num = int(input("Enter the number to be removed from the list: "))

updated_list = rem_occ(lst,num)
print("The updated list: ", updated_list)

# Enter a list of numbers(space-separated): 1 10 9 6 7 2 6 2 6 7 7 5 2
# Enter the number to be removed from the list: 2
# The updated list:  [1, 10, 9, 6, 7, 6, 6, 7, 7, 5]
