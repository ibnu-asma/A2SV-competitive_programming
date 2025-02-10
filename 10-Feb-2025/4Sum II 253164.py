# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sub_total_1 = {}
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sub_total = nums1[i] + nums2[j]
                sub_total_1[sub_total] = sub_total_1.get(sub_total, 0) + 1

        sub_total_2 = {} 
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                target = -(nums3[i] + nums4[j])
                if target in sub_total_1 :
                    count += sub_total_1[target]
                    # sub_total_1[sub_total] = 1
        
        return count
        