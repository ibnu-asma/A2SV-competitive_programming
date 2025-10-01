# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution:
    def longestWord(self, words: List[str]) -> str:

        max_word = ''
        
        def dfs(word):
            nonlocal max_word            
            if word in memo: return memo[word]                        
            
            curr_len = 0
            
            if word == '':
                curr_len = 0                
            elif word[:-1] in words_set:
                curr_len = 1 + dfs(word[:-1])                                
            else:
                curr_len = float('-inf')                
            
            if curr_len > len(max_word) or (curr_len == len(max_word) and word < max_word):                
                max_word = word
                        
            memo[word] = curr_len
            return curr_len
                                           
        words_set = set(words)
        words_set.add('')
        memo = {}
        
        for word in words:
            dfs(word)
            
        return max_word
        