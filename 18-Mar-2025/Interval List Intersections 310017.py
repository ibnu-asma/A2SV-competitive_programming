# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        res = []
        while l < len(firstList) and r < len(secondList):
            min_x = max(firstList[l][0], secondList[r][0])
            max_y  = min(firstList[l][1], secondList[r][1])
            if min_x <= max_y:
                res.append([min_x, max_y])
            if firstList[l][1] <= secondList[r][1]:
                l += 1
            else:
                r += 1
        return res

        