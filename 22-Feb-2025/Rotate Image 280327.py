# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i, cell in enumerate(matrix):
            for j in range(n):
                matrix[i].append(matrix[n - j - 1][i])
        
        print(matrix)
        for i in range(n):
                matrix[i] = matrix[i][n:]

        
        
            

            
            

                
