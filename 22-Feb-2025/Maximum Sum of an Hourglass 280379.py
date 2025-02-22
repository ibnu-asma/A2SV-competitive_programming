# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
    
        maximum = 0
        m, n  = len(grid), len(grid[0])
        
        for i in range(m - 2):
            for j in range(n - 2):
                sum = 0
                for k in range(j, j + 3):
                    sum += grid[i][k]
                for k in range(j, j + 3):
                    sum += grid[i + 2][k]
                sum += grid[i + 1][j + 1]

                maximum = max(sum, maximum)
        
        return maximum


                        


