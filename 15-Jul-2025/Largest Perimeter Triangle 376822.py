# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            sides = nums[i] + nums[i + 1]
            if sides >  nums[i + 2]:
                return sides + nums[i + 2]

        return 0
        