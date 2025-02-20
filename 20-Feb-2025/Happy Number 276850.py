# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        is_visited = set()
        while n not in is_visited:
            is_visited.add(n)
            current_s = str(n)
            current_int = 0
            for i in range(len(current_s)):
                current_int += int(current_s[i])**2
            
            n = current_int
            if current_int == 1:
                return True
        return False
            

        