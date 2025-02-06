# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = []
        negative_nums = []
        for num in nums:
            if num >= 0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)
        

        result = []
        for i in range(len(negative_nums)):
            result.append(positive_nums[i])
            result.append(negative_nums[i])
        return result