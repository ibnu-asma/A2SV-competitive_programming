# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        answer = []
        for c in s:
            if c.isdigit():
                answer.pop()
            else:
                answer.append(c)
        return ''.join(answer)
        