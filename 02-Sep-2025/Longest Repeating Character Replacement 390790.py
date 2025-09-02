# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count, maxFreq, l  = {},  0, 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(r  - l + 1, res)
        return res