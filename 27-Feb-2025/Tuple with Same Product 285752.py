# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        mul = defaultdict(int)
        for i in range(n - 1):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                ans += mul[prod] * 8
                mul[prod] += 1
        return ans

        