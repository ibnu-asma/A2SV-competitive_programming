# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ptr =  0
        for i in range(len(s)):
            if t_ptr < len(t) and t[t_ptr] == s[i]:
                t_ptr += 1
        return len(t) - t_ptr