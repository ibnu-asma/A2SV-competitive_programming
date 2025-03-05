# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lookup = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in lookup:
                return [lookup[diff], i]
            lookup[nums[i]] = i
         