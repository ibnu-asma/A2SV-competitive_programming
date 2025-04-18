# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l, r = 0, 0 
        merged = ""
        while l < len(word1) and r < len(word2):
            if word1[l:] > word2[r:]:
                merged += word1[l]
                l += 1
            else:
                merged += word2[r]
                r += 1
                # how i can choose the character if they are equal
        # print(merged)
        merged += word1[l:] if l < len(word1) else word2[r:]
        return merged

        