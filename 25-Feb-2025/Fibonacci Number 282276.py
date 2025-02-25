# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        def seq(t):
            if t <= 1:
                return t
            return seq(t - 1) + seq(t - 2)
        return seq(n)
    
        