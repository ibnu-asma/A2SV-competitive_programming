# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def binary_search(self, l, r, nums, target):
        if l > r:
            return -1
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(l, mid - 1, nums, target)
        return self.binary_search(mid + 1, r, nums, target)
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l, r = 0, N - 1
        return self.binary_search(l, r, nums, target)