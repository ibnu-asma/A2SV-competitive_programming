# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        