# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = defaultdict(int)
        
        for i, num in enumerate(nums):
            frequency[num] += 1
        
        frequencySortedByValue = dict(sorted(frequency.items(), key=lambda x:x[1], reverse=True))
        return list(frequencySortedByValue.keys())[:k]
        
        
            