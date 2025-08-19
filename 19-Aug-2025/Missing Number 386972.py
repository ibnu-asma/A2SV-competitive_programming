# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur, res = 0, 0
        for n in nums:
            cur ^= n
        for i in range(len(nums) + 1):
            res ^= i
        return res^cur
        