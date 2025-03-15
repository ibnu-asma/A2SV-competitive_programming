# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums1) == m:
            nums1.extend([0] * n)
    
        if m == 0:
             for i in range(n):
                nums1[i] = nums2[i]
        else:
            p1 = m - 1
            p2 = n - 1

            last_index = len(nums1) - 1

            while p1 >= 0 and p2 >= 0: # 2
                if nums2[p2] > nums1[p1]:
                    nums1[last_index] = nums2[p2]
                    p2 -= 1
                else:
                    nums1[last_index] = nums1[p1]
                    p1 -= 1 # m = 0
                last_index -= 1

            while p2 >= 0:
                nums1[last_index] = nums2[p2]
                p2 -= 1
                last_index -= 1

        print(nums1)