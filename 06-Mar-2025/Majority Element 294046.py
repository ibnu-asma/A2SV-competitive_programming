# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem, count, n = 0, 0, len(nums)

        for i in range(n):
            if count == 0:
                elem = nums[i]
                count += 1
            elif elem != nums[i]:
                count -= 1
            else:
                count += 1
        return elem
        