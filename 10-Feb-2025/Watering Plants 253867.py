# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        original_capacity = capacity
        for i in range(len(plants)):
            if plants[i] <= capacity:
                steps += 1
                capacity -= plants[i]
            else:
                steps += ((2* i) + 1)
                capacity = original_capacity - plants[i]
        return steps
            

        