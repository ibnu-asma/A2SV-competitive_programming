# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        n = num
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2

        flipped = ""
        for bit in binary:
            if bit == "1":
                flipped += "0"
            else:
                flipped += "1"

        res = 0
        for bit in flipped:
            res = res * 2 + int(bit)

        return res
