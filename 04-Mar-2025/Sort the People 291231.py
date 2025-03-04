# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for j in range(n):
            for i in range(n - 1, j, -1):
                if heights[i] > heights[i - 1]:
                    heights[i], heights[i - 1] = heights[i - 1], heights[i] 
                    names[i], names[i - 1] = names[i - 1], names[i]
        return names

        