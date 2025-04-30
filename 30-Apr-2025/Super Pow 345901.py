# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        c = 0
        c = int("".join(map(str, b)))
        return pow(a, c, 1337)




        