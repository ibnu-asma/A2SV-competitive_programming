# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n*(n + 1))//2
        current_sum = 0
        for num in nums:
            current_sum += num
        return total_sum - current_sum
        
        