# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sub_set = []
        res = []
        def power_set(i, sub_set):
            if i == n:
                res.append(sub_set[:])
                return  
            sub_set.append(nums[i])
            power_set(i + 1, sub_set)
            sub_set.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            power_set(i + 1, sub_set)

        power_set(0,sub_set)
        
        return res
                
        