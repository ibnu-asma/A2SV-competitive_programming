# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-a for a in piles]
        heapq.heapify(piles)
        for i in range(k):
            heapq.heapreplace(piles, piles[0] // 2)
        return -sum(piles)
        