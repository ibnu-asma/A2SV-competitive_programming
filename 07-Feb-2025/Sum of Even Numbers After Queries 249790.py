# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []

        even = 0
        for num in nums:
            if num % 2 == 0:
                even += num
      
        print(result)



        for i, query in enumerate(queries):
            current_value = nums[query[1]]
            new_value = query[0]
            total_value = current_value + new_value
            nums[query[1]] = total_value
            if current_value % 2 == 0:
                even -= current_value
            if total_value % 2 == 0:
                even += total_value
            
            result.append(even)
           

        return result
                
            
           
                    

