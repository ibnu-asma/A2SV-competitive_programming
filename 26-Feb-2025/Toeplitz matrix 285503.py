# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        diagonal = n + m - 1
    
        for i in range(diagonal):
            x = n - 1 - i if i < n  else 0 
            y = 0 if i < n else i - n + 1

            while x < n - 1 and y < m - 1:
                if matrix[x][y] != matrix[x + 1][y + 1]:
                    return False
                x += 1
                y += 1
        return True
            


            

            