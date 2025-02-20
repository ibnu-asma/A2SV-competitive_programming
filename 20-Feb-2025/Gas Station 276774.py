# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start_index = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start_index =  i + 1
            
        return start_index

             



        # for i in range(n):
        #     totalFuel = 0
        #     stopCount = 0
        #     j = i
        #     while stopCount < n:
        #         totalFuel += gas[j % n] - cost[j % n]
        #         if totalFuel < 0:
        #             break
        #         stopCount += 1
        #         j += 1
        #     if stopCount == n and totalFuel >= 0:
        #         return i
        # return -1
         
        