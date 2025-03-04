# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for j in range(n):
            flag = 0
            for i in range(n):
                if nums[j] == nums[i] and i != j:
                    flag = 1
                    break
            if not flag:
                return nums[j]