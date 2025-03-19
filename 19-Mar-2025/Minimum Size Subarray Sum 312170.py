# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, n = 0, 0, len(nums)
        min_len = float('inf')
        cur_sum = 0
        while r < n:
            cur_sum += nums[r]
            while cur_sum >= target:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0