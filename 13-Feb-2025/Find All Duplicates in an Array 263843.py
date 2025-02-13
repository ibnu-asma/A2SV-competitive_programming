# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                result.append(nums[i])
        return result
            
