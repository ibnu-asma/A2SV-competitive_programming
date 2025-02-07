# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        max_occurence = max(counts,key=counts.get)
        
        return counts[max_occurence] > 1
        