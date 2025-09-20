# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_val = max(piles)
        freq = [0] * (max_val + 1)

        for i in piles:
            freq[i] += 1

        coins = 0
        chance = len(piles) // 3
        turn = 1
        i = max_val

        while chance != 0:
            if freq[i] > 0:
                if turn == 1:
                    turn = 0
                else:
                    chance -= 1
                    turn = 1
                    coins += i
                freq[i] -= 1
            else:
                i -= 1

        return coins
        