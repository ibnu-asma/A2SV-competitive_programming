# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count = 0
        string1 = [x for x in s1]
        string2 = [x for x in s2]

        print(string1)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count == 2:
                    temp = string1[first_index]
                    string1[first_index] = string1[i]
                    string1[i] = temp
                    print(string1, string2)
                    if string1 == string2:
                        return True
                    return False
                else:
                    first_index = i
        return False    
        