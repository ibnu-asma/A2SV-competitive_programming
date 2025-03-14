# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        temp = set(nums)
        max_length = -1
        for num in nums:
            length = 1
            while num**2 in temp:
                length += 1
                num = num ** 2
                max_length = max(length, max_length)
        return -1 if max_length < 2 else max_length


        