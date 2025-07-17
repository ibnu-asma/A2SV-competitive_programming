# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        M = len(height)
        l, r = 0, M - 1
        maxArea = 0
        while l < r:
            width = r - l
            area = width * min(height[l], height[r])
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        