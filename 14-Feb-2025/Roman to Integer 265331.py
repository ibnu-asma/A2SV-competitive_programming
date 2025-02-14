# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        temp = reversed(s)
        is_special = False
        special = ''
        for i, c in enumerate(temp):
            if is_special:
                if special == 'V' or special == 'X':
                    if c == 'I':
                        result -= roman_dict['I']
                        is_special = False
                        continue
                elif special == 'L' or special == 'C' :
                    if c == 'X':
                        result -= roman_dict['X']
                        is_special = False
                        continue
                elif special == 'D' or special == 'M':
                    if c == 'C':
                        result -= roman_dict['C']
                        is_special = False
                        continue
                is_special = False

            if roman_dict[c] % 5 == 0:
                is_special = True
                result += roman_dict[c]
                special = c
            else:
                result += roman_dict[c]
        return result