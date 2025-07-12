# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
       
        # print(type(distances))

        for x, y in points:
            distance = pow(x,2) + pow(y, 2)
            distances.append([distance, x , y])

        heapq.heapify(distances)

        
        res = []
        for i in range(k):
            dis, x, y = heapq.heappop(distances)
            res.append([x, y])
        
        return res



        