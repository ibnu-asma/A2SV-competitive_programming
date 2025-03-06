# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = collections.defaultdict(int)
        n = len(nums)
        for num in nums:
            lookup[num] += 1

        for key, value in lookup.items():
            if value > n/2:
                return key
        return - 1
        