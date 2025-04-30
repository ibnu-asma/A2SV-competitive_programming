# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        width = 0
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                width = max(width, j - stack[-1])
                stack.pop()
        return width