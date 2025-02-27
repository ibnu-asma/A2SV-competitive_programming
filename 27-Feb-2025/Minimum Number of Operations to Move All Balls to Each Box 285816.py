# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lookup = []
        n = len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == '1':
                lookup.append(i)
        ans = []
        for i in range(n):
            distance = 0
            for j in range(len(lookup)):
                distance += abs(lookup[j] - i)
            ans.append(distance)
        return ans
