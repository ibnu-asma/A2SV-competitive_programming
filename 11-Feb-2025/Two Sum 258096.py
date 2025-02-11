# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        for i, num in enumerate(nums):
            diff  = target - num
            if diff in result_dict:
                return [result_dict[diff], i]
            result_dict[num] = i
        