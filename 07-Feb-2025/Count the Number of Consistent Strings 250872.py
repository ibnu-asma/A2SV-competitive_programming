# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count  = 0
        allowed_chars  = set(allowed)
        for word in words:
            is_consistent = True
            current_word = set(word)
            for wor in current_word:
                if wor not in allowed_chars:
                    is_consistent = False
                    break
            if  is_consistent:
                count += 1
            
        return count