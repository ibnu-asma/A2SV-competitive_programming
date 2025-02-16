# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_list = set()
        for x, y in ranges:
            for i in range(x, y + 1):
                range_list.add(i)
        print(range_list)
        
        for i in range(left, right + 1):
            if i not in range_list:
                return False
        return True
        