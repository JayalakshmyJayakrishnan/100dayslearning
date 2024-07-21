class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)                                                     # Get the number of rows
                                                                       # Check if the matrix is an identity matrix
        for i in range(N):
            for j in range(len(A[i])):
                if (i == j and A[i][j] != 1) or (i != j and A[i][j] != 0):
                    return 0
        return 1

                                                                       #Sample matrix
if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(solution.solve(matrix))                                      #Output: 1
