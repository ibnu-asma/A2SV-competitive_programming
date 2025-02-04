# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_length  = 0
        string_list = s.split(" ")
        for string in string_list:
            current_length = len(string)
            if  current_length > max_length:
                max_length = current_length
        
        result = []
        for i in range(max_length):
            current_string = []
            for j in range(len(string_list)):
                if i < len(string_list[j]):
                    current_string.append(string_list[j][i])
                else:
                    current_string.append(" ")


            result.append("".join(current_string).rstrip())
        
        return result
        



        

        