# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, r = 0, 0
        longest = 0
        while r < len(s):
            while  s[r]  in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest