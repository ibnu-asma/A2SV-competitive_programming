# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        count_img1 = []
        count_img2 = []
        d = collections.defaultdict(int)
        n = len(img1)
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    count_img1.append((i, j))
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    count_img2.append((i, j))
        
        ans = 0
        for t1 in count_img1:
            for t2 in count_img2:
                t3 = (t2[0] - t1[0], t2[1]- t1[1])
                d[t3] += 1
                ans = max(ans, d[t3])
        return ans
        