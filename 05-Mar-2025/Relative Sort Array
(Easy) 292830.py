# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n, m= len(arr2), len(arr1)

        res = []
        for i in range(n):
            curr = arr2[i]
            for j in range(m):
                if curr ==arr1[j]:
                    res.append(curr)
                    arr1[j] = -1
        arr1.sort()
        for num in arr1:
            if num != -1:
                res.append(num)
        return res
        
        