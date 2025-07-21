# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        M = len(temperatures)
        answer = [0]*M
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                answer[stackIdx] = idx - stackIdx
            stack.append((temp, idx))
        return answer