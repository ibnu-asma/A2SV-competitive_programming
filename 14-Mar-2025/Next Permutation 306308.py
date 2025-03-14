# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        n  = len(nums)
        for i in range(n - 1, 0, -1 ):
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break
        if idx != -1:
            for i in range(n - 1, idx - 1, -1):
                if nums[i] > nums[idx]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    break
            print(nums)
            l, r = idx + 1, n - 1
            while l < r: 
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
                r -= 1
        else:
            nums.sort()

        print(nums)
            