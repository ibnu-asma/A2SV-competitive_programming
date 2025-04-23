# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []
        for direc in directories:
            if direc == '.' or not direc:
                continue
            elif direc == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(direc)
        return '/' + '/'.join(stack)
        
        