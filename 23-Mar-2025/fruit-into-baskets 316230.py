# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i  = defaultdict(int), 0 
       
        for j, v in enumerate(fruits):
            count[v] += 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]]  == 0:
                    del count[fruits[i]] 
                i += 1
        return j - i + 1
            

            