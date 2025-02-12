# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        counts = Counter(nums)
        return list(filter(lambda k: counts[k] > freq, counts))