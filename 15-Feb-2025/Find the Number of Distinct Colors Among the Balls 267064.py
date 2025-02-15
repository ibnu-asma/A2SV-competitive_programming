# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        colors = defaultdict(int)
        result = []
        for x, y in queries:
            if x in colors:
                freq[colors[x]] -= 1
                if freq[colors[x]] == 0:
                    del freq[colors[x]]
            freq[y] += 1
            colors[x] = y   
            result.append(len(freq)) 
        print(freq)        
        return result

        