# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count, l, r, n = 0, 0, 0, len(s)
        freq = {'a':0, 'b':0, 'c': 0}

        while r < n:
            freq[s[r]] += 1
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                freq[s[l]] -= 1
                count += n - r
                l += 1
            r += 1
        return count

        