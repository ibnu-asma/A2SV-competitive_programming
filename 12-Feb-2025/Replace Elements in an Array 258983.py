# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

from collections import defaultdict
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        lookup  = {}

        for i, num in enumerate(nums):
            lookup[num] = i
        
        for i, op in enumerate(operations):
            indx = lookup[op[0]]
            nums[indx] = op[1]
            lookup[op[1]] = indx
            lookup.pop(op[0])
        return nums