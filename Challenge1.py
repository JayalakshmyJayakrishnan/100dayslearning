class Solution:
  
    # @param A : string
    # @param B : string
    # @return a strings
  
    def solve(self, A, B):
      return A + B
      
#Creating an instance of the 'Solution' class
      solution = Solution()

# Define the input strings
     
      A = "interview"
      B = "bit"
#Call the solve method with A and B as arguments    
      result = solution.solve(A,B)

 # Print the result
      print(result)

#Output: interviewbit
