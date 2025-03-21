# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        count = 0
        l = 0
        maxi = 1
        for r in range(1, len(s)):
            if s[r] == s[r - 1]:
                count += 1
            while count > 1:
                if s[l] == s[l + 1]:
                    count -= 1
                l += 1
            maxi = max(maxi, r - l + 1)
        return maxi

        


        