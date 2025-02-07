# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key=counts.get)
        
        