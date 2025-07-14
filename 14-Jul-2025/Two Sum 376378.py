# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = defaultdict(int)

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in visited:
                return [i, visited[comp]]
            visited[nums[i]] = i
