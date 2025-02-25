# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])

        is_first_row_has_zero = 0 in matrix[0]
        is_first_col_has_zero = 0 in [matrix[i][0] for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if is_first_row_has_zero:
            for i in range(m):
                matrix[0][i] = 0
        if is_first_col_has_zero:
            for i in range(n):
                matrix[i][0] = 0
        

        

                
        