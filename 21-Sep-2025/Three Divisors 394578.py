# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1: return False
        
        x = int(sqrt(n))
        if x*x != n: return False 
        
        for i in range(2, int(sqrt(x))+1): 
            if x % i == 0: return False 
        return True
        