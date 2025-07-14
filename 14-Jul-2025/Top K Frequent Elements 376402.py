# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        res = sorted(freq, key=freq.get, reverse=True)
        ans = []
        i = 0
        while k > 0:
            ans.append(res[i])
            i += 1
            k -= 1
        return ans