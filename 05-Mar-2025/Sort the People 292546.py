# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if heights[j] >  heights[idx]:
                    idx = j
            heights[i], heights[idx] = heights[idx], heights[i]
            names[i], names[idx] = names[idx], names[i]
        return names
        

        