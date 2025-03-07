# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        first_max = max(nums)
        idx = len(nums) - 1
        while first_max == nums[idx] and idx >= 0:
            idx -= 1
        second_max = nums[idx]
        while second_max == nums[idx] and idx >= 0:
            idx -= 1
        
        return nums[idx]

        
        
                


        