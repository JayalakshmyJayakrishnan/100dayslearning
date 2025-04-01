# Function to add two matrices
def add_matrices(mat1, mat2):
    result = []  

    for i in range(len(mat1)):  
        row = []  
        for j in range(len(mat1[0])):  
            row.append(mat1[i][j] + mat2[i][j])  
        result.append(row)  

    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


print("Enter the first matrix row by row:")
matrix1 = []
for i in range(rows):
    matrix1.append(list(map(int, input().split()))) 


print("Enter the second matrix row by row:")
matrix2 = []
for i in range(rows):
    matrix2.append(list(map(int, input().split())))  


sum_matrix = add_matrices(matrix1, matrix2)


print("\nSum of matrices:")
for row in sum_matrix:
    print(*row)  
