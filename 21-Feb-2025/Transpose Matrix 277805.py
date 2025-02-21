# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    
        ans = [[] for _ in range(len(matrix[0]))]
        i = 0
        for col in  range(len(matrix[0])):
            for row in range(len(matrix)):
                ans[col].append(matrix[row][col])
    
        return ans
        
            