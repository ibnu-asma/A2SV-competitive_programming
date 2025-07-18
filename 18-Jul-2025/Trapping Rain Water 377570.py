# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:

        M = len(height)
        if M == 0:
            return 0
        res = 0
        leftMax = [0] * M
        rightMax = [0]* M
        leftMax[0] = height[0]
        for i in range(1, M):
            leftMax[i] = max(leftMax[i - 1], height[i])


        rightMax[M - 1] = height[M - 1]
        for i in range(M - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        for i in range(M):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
        