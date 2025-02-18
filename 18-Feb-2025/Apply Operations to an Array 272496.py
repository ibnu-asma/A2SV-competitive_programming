# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) -1):
            if nums[i] != nums[i + 1]:
                continue
        
            nums[i] = 2* nums[i]
            nums[i + 1] = 0

        result = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                continue
            result.append(nums[i])

        while  count > 0:
            result.append(0)
            count -= 1
        return result
