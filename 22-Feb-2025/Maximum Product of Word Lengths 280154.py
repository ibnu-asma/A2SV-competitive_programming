# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_char(str1, str2):
            set1 = set(str1)
            set2 = set(str2)
            return set1.isdisjoint(set2)
        max_length = 0
        for i,word in enumerate(words):
            current_length = 0
            for j in range(i + 1, len(words)):
                if no_common_char(word, words[j]):
                    current_length = len(word) * len(words[j])
                max_length = max(current_length, max_length)
        return max_length

               
        


        
        
        
        