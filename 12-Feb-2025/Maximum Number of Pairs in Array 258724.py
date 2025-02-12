# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_dict = defaultdict(list)

        for i, num in enumerate(nums):
            count_dict[num].append(i)
        count = 0
        for key, value in count_dict.items():
            count += len(value) // 2
        return [count, len(nums) - (2 * count)]
        
        