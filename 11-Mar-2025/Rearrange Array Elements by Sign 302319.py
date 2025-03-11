# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        n = len(nums)
        res = []
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        l =  0
        while l < n // 2:
            res.append(positive[l])
            res.append(negative[l])
            l += 1
        return res
        