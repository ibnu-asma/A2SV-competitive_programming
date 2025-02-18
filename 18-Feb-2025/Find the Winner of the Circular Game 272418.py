# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = [i for i in range(1, n + 1)]
        current_pos = 0
        while n >  1:
            current_pos = (current_pos + k -1) % n
            friends.pop(current_pos)
            n -= 1

        return friends[0]
                
