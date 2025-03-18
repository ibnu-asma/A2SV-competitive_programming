# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        l, r = 0, k
        # aver = 0
        maxi = current_sum
        while r < len(nums):
            current_sum = current_sum - nums[l] + nums[r]
            maxi = max(maxi, current_sum)
            l += 1
            r += 1
        return maxi/k
        

            
        