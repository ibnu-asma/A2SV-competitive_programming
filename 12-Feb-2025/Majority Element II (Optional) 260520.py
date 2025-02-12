# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        counts = Counter(nums)
        return list(filter(lambda k: counts[k] > freq, counts))


        