# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1  
                if count > 1:
                    return False
                
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                if i > 1 and nums[i - 2] > nums[i - 1]:
                    nums[i - 1] = temp
                    nums[i] = nums[i - 1]
                elif i > 1 and nums[i - 2] > nums[i - 1]:
                    return False
                else:
                    continue
    

        return True
         