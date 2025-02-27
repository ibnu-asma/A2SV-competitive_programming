# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        negatives = 0
        min_abs = float('inf')
        total = 0
        for i in range(n):
            for j in range(n):
                current = matrix[i][j]
                min_abs = min(min_abs, abs(current))
                total += abs(current)
                if current < 0:
                    negatives += 1
        return total if negatives % 2 == 0 else total + (-2*min_abs)