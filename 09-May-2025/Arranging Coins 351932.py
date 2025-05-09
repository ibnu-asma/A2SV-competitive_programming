# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start  = 1
        end = n
        ans = 0
        mid = 0
        while start <= end:
            mid = (start + end)//2
            coin_count = (mid*(mid + 1))//2
            if (coin_count <= n):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans