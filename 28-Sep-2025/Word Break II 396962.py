# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        results = []
        self._backtrack(s, word_set, [], results, 0)
        return results

    def _backtrack(
        self,
        s: str,
        word_set: set,
        current_sentence: List[str],
        results: List[str],
        start_index: int,
    ):
        if start_index == len(s):
            results.append(" ".join(current_sentence))
            return

        for end_index in range(start_index + 1, len(s) + 1):
            word = s[start_index:end_index]
            if word in word_set:
                current_sentence.append(word)
                self._backtrack(
                    s, word_set, current_sentence, results, end_index
                )
                current_sentence.pop()