def sep(numbers):
    even = tuple(num for num in numbers if num%2==0)
    odd =  tuple(num for num in numbers if num%2!=0)
    
    return even, odd
    
numbers_tuple = tuple(map(int, input("Enter the numbers: ").split()))
even_t, odd_t = sep(numbers_tuple)

print("Even numbers: ", even_t)
print("Odd numbers: ", odd_t)

# OUPUT
# Enter the numbers: 1 2 3 4 5 6 7 8 9 10
# Even numbers:  (2, 4, 6, 8, 10)
# Odd numbers:  (1, 3, 5, 7, 9)
