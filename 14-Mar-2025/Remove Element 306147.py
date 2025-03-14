# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        n = len(nums) - 1
        while r <= n:
            if nums[r] == val:
                r += 1
            else:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r += 1
        return l

                




        