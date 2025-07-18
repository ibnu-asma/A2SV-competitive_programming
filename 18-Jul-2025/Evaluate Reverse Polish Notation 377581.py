# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['*', '-', '+', '/']
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                res = self.getResult(token, first, second)
                stack.append(res)
        return stack[-1]
            
    def getResult(self, op, val1, val2):
        if op == '*':
            return val1*val2
        elif op == '/':
            return int(float(val1) / val2)
        elif op == '+':
            return val1 + val2
        else:
            return val1 - val2
            
            
        