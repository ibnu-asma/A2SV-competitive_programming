# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        d = k % n
        temp = []
        for i in range(n - d, n):
            temp.append(nums[i])
        j = n -1
        for i in range(n -d - 1, -1, -1):
            nums[j] = nums[i]
            j -= 1

        for i in range(len(temp)):
            nums[i] = temp[i]
