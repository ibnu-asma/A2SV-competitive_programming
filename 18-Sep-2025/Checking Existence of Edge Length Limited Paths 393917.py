# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        s = ''.join(map(chr, range(n)))
        *map(list.append, queries, count()),
        for u, v, d, *j in sorted(queries + edgeList, key=itemgetter(2)):
            if j: queries[j[0]] = s[u] == s[v]
            else: s = s.replace(s[u], s[v])
        return queries
            