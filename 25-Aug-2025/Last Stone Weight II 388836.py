# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        pre_state = {0}
        for elem in stones:
            state = set()
            for prev in pre_state:
                state.add(elem + prev)
                state.add(abs(prev - elem))
            pre_state = state
        return min(pre_state)