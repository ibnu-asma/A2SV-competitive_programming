# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index
               
            stack.append(i)
        return res
        