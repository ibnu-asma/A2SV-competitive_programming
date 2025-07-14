# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

from heapq import heappop, heappush
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        M = len(nums1)
        N = len(nums2)
        res = []
        visited = set()

        minHeap = [[nums1[0] + nums2[0], 0,0]]
        visited.add((0,0))
        while k > 0 and minHeap:
            val, i, j = heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            k -= 1
            if i + 1 < M and (i + 1, j) not in visited:
                heappush(minHeap, [nums1[i + 1] + nums2[j], i + 1, j])
                visited.add((i + 1, j))
            if j + 1 < N and (i, j + 1) not in visited:
                heappush(minHeap, [nums1[i] + nums2[j + 1], i, j + 1])
                visited.add((i, j + 1))

        return res