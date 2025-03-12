# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(a, l, r):
            while l < r:
                if a[l] != a[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True
                
        