# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [0 for _ in range(n+2)]
        dp[0] = sys.maxsize  # set left boundry as int max
        dp[n+1] = sys.maxsize  # set right boundry as int max

        for i in range(n):
            tmp = dp.copy()
            for j in range(n):
                # min (prev[j-1], prev[j], prev[j+1])
                # added 1 to j to correctly point idx in prev values list
                tmp[j+1] = matrix[i][j] + min(dp[j], dp[j+1], dp[j+2])
            dp = tmp
        return min(dp)
        