# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        tags = {'{': '}', '(':')', '[':']'}
        stack = []
        for c in s:
            if c in tags:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if tags[top] != c:
                    return False
            
        return True if not stack else False
        