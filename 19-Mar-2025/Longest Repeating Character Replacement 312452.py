# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = defaultdict(int)
        res  = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            cur_len = r - l + 1
            if (cur_len - max_freq) > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

