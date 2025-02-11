# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        remainder = 0
        while num > 0:
            digit = num % 10
            remainder = (remainder * 10) +  digit
            num = num // 10
        if (remainder == x):
            return True
        return False
            
            