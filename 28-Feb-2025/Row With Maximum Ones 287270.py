# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

from collections import defaultdict
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for i, m  in enumerate(mat):
            count[i] = m.count(1)
        ans = max(count, key=count.get)
        return [ans,count[ans]]
        