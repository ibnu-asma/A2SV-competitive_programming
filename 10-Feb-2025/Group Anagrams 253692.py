# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            print(sorted_s)
            frequency[sorted_s].append(s)
        
        result  = []

        for item in frequency.values():
            result.append(item)
        return result
        