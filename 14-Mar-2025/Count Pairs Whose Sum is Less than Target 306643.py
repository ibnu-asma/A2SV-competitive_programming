# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            sum_2 = nums[l]  + nums[r]
            if sum_2 >= target:
                r -= 1
            else:
                count += r - l
                l += 1
        return count
            
        