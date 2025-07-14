# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            cur = tuple(sorted(s))
            anagram[cur].append(s)
        res = []

        for group in anagram:
            res.append(anagram[group])
        return res
        

        