# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        M = len(s)
        l, r = 0, M - 1
        while l < r:
            while not self.isAlphaNum(s[l]) and l < M - 1:
                l += 1
            while not self.isAlphaNum(s[r]) and r >= 0:
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True






    def isAlphaNum(self, ch):
        return  ((ord(ch) >= ord('a') and ord(ch) <= ord('z'))
            or (ord(ch) >= ord('A') and ord(ch) <= ord('Z'))
            or (ord(ch) >= ord('0') and ord(ch) <= ord('9')))
        