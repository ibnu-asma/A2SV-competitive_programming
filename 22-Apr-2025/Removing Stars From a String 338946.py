# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c == "*":
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)

        