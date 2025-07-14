# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1  

        return t_dict == s_dict
    