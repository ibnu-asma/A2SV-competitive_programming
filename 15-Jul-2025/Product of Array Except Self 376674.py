# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        sufix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
        print(prefix)
        for i in range(len(nums) - 1, 0, -1):
            sufix.append(sufix[-1]* nums[i])
        print(sufix)

        res = []
        n = len(nums) - 1
        for i in range(len(nums)):
            res.append(prefix[i] * sufix[n])
            n -= 1
        return res