# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        res = 0
        n = len(piles) // 3
        idx = 1
        while n > 0:
            res +=  piles[(2 * idx) - 1]
            idx += 1
            n -= 1 
        return res