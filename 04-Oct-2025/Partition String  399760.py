# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        n = len(s)
        segments = []
        seen = set()
        i = 0

        while i < n:
            found = False
            cur = ''
            for j in range(i, n):
                cur += s[j]
                if cur not in seen:
                    found = True
                    segments.append(cur)
                    seen.add(cur)
                    i = j + 1
                    break
            if not found:
                break

        return segments
            