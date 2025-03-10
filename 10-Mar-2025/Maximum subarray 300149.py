# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, maximum = 0, float('-inf')
        start, end = -1, -1
        for i ,num  in enumerate(nums):
            if sum < 0:
                start = i
            sum += num
            maximum = max(sum, maximum)

            if sum < 0:
                sum = 0
        return maximum


        