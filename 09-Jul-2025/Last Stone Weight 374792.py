# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap =  []
        heapq.heapify(maxHeap)
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            combined = first - second
            if combined < 0:
                combined = -combined
            if combined > 0:
                heapq.heappush(maxHeap, -combined)
            
        return -maxHeap[0] if maxHeap else 0

        