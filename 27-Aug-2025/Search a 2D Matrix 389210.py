# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            m = (top + bot)//2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        if not (top <= bot):
            return False
        cur = (top + bot)//2
        l, r = 0, len(matrix[cur])
        while l <= r:
            m = (l + r)//2
            if target == matrix[cur][m]:
                return True
            elif target > matrix[cur][m]:
                l = m + 1
            else:
                r = m - 1
        return False
