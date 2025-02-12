# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric_only =  ""
        for c in s:
            if c.isalnum():
                alpha_numeric_only += c.lower()
            
        result = self.check_palindrome(0, alpha_numeric_only)
        return result

    
    def check_palindrome(self, l:int, s:str) -> bool:
        if l >= len(s) // 2:
            return True
        if s[l] != s[-l - 1]:
            return False
        return self.check_palindrome(l + 1, s)
    

