# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_starts = sorted([(interval[0], idx) for idx, interval in enumerate(intervals)], key=lambda x: x[0])
        
        start_values = [start for start, idx in sorted_starts]
        
        res = []
        for i in range(len(intervals)):
            end_i = intervals[i][1]
            index_in_sorted = bisect.bisect_left(start_values, end_i)
            if index_in_sorted < len(start_values):
                original_index = sorted_starts[index_in_sorted][1]
                res.append(original_index)
            else:
                res.append(-1)
        return res