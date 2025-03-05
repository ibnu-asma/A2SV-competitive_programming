# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(3):
            for j in range(idx, len(nums)):
                if nums[j] == i:
                    nums[j], nums[idx] = nums[idx], nums[j]
                    idx += 1

        