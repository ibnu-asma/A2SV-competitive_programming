# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_s_to_t = {}
        mapped_chars = set()

        for char_s, char_t in zip(s, t):
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_chars:
                    return False
                mapping_s_to_t[char_s] = char_t
                mapped_chars.add(char_t)

        return True

        