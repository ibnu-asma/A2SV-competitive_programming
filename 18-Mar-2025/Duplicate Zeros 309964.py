# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        idx = -1
        is_zero = False
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                count += 2
                is_zero = True
            else:
                count += 1
                
            if count >= n and is_zero:
                idx = i
                break

        print(idx, count)
        if idx != -1:
            temp = n
            n = n -  1
            while n >= 0:
                if count > temp:
                    arr[n] = arr[idx] 
                    idx -= 1
                    n -= 1
                    count = 0
                elif arr[idx] != 0:
                    arr[n] = arr[idx]
                    idx -= 1
                    n -= 1
                else:
                    arr[n] = 0
                    arr[n - 1] = 0
                    n -= 2
                    idx -= 1
        print(arr)
                


        print(idx)
        