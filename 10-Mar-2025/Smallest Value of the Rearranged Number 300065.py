# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        temp = num if num > 0 else -num
        res = [int(t) for t in str(temp)]
        res.sort()
        i = 0
        print(res)
        while i < len(res):
            if res[i] != 0:
                break
            i += 1
        if num > 0:
            res[0], res[i] = res[i], res[0]
        done = ''
        for c in res:
           done += str(c)
        print(done)
        if num > 0:
            return int(done)
        else:

            return -int("".join(sorted(done, reverse=True)))
        