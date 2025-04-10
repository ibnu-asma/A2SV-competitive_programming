# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l =  0
        target = sum(nums) - x
        max_window  = -1
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_window = max(max_window, r - l + 1)
            
        return -1 if max_window == -1 else len(nums) - max_window
        