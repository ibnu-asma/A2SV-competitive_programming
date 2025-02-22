# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        def dist(x, y):
            return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])
        for i , x in enumerate(points):
            dis = collections.defaultdict(int)
            for j, y in enumerate(points):
                if i == j:
                    continue
                distance = dist(x, y)
                dis[distance] += 1
            
            for d in dis.keys():
                count += dis[d] * (dis[d] - 1)
        return count
        