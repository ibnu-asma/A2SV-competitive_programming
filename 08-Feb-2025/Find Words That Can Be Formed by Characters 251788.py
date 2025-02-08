# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = Counter(chars)
        length = 0
        for word in words:
            is_good = True
            word_dict = Counter(word)

            for char, value in word_dict.items():
                if chars_dict[char] < value:
                    is_good = False
                    break
            if is_good:
                length += len(word)
            is_good = True
        
        return length
        
        