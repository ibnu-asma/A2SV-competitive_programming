# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = Counter(p)
        l, r = 0, len(p) - 1
        res = []
        while r < len(s):
            cur_freq = Counter(s[l:r + 1])
            if cur_freq == freq:
                res.append(l)
            l += 1
            r += 1
        return res
            

        