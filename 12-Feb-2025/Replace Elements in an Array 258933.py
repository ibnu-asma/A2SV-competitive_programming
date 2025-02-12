# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

from collections import defaultdict
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dublicate = set(nums)
        final_values = defaultdict(lambda : -1)
        for op in reversed(operations):
            place, value = op[0], op[1]
            final_values[place] = final_values.get(value, value)
        for i, num in enumerate(nums):
            if num in final_values:
                nums[i] = final_values[num]
           
        print(final_values)
        print(nums)
        return nums
        return []
            



