# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        for a in nums:
            while a:
                gcd, a = a, gcd % a
        return gcd == 1
        