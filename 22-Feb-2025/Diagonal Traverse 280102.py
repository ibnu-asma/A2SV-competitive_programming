# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n, m  = len(mat), len(mat[0])
        intermidiate = []
        res, intermidiate = [], []

        for d in range(n + m - 1):
            intermidiate.clear()
            r, c = 0 if d < m else d - m + 1, d if d < m else m - 1

            while r < n and c > -1:
                intermidiate.append(mat[r][c])
                r += 1 
                c -= 1
            if d % 2 == 0:
                res.extend(intermidiate[::-1])
            else:
                res.extend(intermidiate)
        return res

            





        