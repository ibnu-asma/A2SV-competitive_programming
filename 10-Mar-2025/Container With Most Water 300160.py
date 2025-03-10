# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        max_area = 0

        while l < r:
            width = r - l

            current_area  = width * min(height[r], height[l])
            max_area = max(max_area, current_area)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return max_area
            
        