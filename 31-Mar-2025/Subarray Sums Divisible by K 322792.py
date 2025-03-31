# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixMod, res = 0, 0
        modGroups = [0]* k
        modGroups[0] = 1
        for num in nums:
            prefixMod = (prefixMod + num % k + k )% k
            res += modGroups[prefixMod]
            modGroups[prefixMod] += 1
        return res

        