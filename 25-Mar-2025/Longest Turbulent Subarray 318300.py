# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        ans = 1
        anchor = 0

        for i in xrange(1, N):
            c = cmp(arr[i-1], arr[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(arr[i], arr[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
        