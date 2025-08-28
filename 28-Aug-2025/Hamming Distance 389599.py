# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xb, yb, ans = f'{x:032b}', f'{y:032b}', 0
        return sum(i != j for i, j in zip(xb, yb))