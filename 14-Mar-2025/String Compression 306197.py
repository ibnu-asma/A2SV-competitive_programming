# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, res = 0, 0
        while i < len(chars):
            groupLength = 1
            while (i + groupLength < len(chars) and chars[i + groupLength] == chars[i]):
                groupLength += 1
            chars[res] = chars[i]
            res += 1
            if groupLength > 1:
                str_rep = str(groupLength)
                chars[res: res + len(str_rep)] = list(str_rep)
                res += len(str_rep)
            i += groupLength
        return res
                


        