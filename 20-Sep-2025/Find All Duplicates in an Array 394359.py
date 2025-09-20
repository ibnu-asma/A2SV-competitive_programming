# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r = [abs(x) for x in nums if nums[abs(x) - 1] < 0 or (nums.__setitem__(abs(x) - 1, -nums[abs(x) - 1]) is None and 0)]
        return r
        