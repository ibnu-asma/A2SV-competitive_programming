# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        counts = Counter(nums)
        func = lambda k: counts[k] > freq
        result = list(filter(func, counts))
        return result

        