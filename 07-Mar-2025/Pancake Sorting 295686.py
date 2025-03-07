# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(a, k):
            i = 0
            while i < k / 2:
                a[i], a[k  - 1 - i] = a[k -1 - i], a[i]
                i += 1
        res = []
        num_to_sort = len(arr)
        while num_to_sort > 0:
            idx = arr.index(num_to_sort)
            if idx != num_to_sort - 1:
                if idx != 0:
                    res.append(idx + 1)
                    flip(arr, idx + 1)
                res.append(num_to_sort)
                flip(arr, num_to_sort)
            num_to_sort -= 1
        return res
            

        