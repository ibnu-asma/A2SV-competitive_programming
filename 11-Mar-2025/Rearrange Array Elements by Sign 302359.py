# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 1
        n = len(nums)
        res = [0]*n
        for i, num in enumerate(nums):
            if num >= 0:
                res[positive] = num
                positive += 2
            else:
                res[negative] = num
                negative += 2
        return res
        