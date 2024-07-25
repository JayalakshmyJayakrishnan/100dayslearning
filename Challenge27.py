from itertools import product

#Taking input and converting it to a list of integers for A
A = list(map(int, input().split()))

#Taking input and converting it to a list of integers for B
B = list(map(int, input().split()))

#Generating the Cartesian product of A and B, and printing it
print(*list(product(A, B)))
