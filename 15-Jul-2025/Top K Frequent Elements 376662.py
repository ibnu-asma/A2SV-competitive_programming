# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(freq)
        res = []

        for i in range(len(freq) - 1, 0, -1):
            cur = freq[i]
            print(cur)
            for item in cur:
                res.append(item)
                if len(res) == k:
                    return res
       
        
            