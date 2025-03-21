# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, n = 0, len(nums)
        temp = set()
        score = 0
        for r in range(n):

            while nums[r] in temp:
                temp.remove(nums[l])
                l += 1
            temp.add(nums[r])
            score = max(score, sum(temp))
        return score
            

