# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        rabbits = 0
        print(freq)
        for ans in answers:
            if ans == 0:
                rabbits += 1
            elif freq[ans] > 0:
                rabbits += 1 + ans
                freq[ans] -= (ans  + 1)
        
        return rabbits