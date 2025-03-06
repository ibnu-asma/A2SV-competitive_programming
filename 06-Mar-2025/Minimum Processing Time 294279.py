# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        time_taken = 0
        for i in range(len(processorTime)):
            task_idx = 4*i
            curr = tasks[task_idx] + processorTime[i]
            time_taken = max(time_taken, curr)
        return time_taken
