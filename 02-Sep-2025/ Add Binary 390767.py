# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_b = int(b, 2)
        dec_a = int(a, 2)
        sum_dec = dec_a + dec_b
        sum_bin = bin(sum_dec)
        return sum_bin[2:]
        