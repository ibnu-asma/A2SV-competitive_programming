# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                cur_str = ""
                while stack[-1] != '[':
                    cur_str = stack.pop() + cur_str
                stack.pop()
                cur_num = ""
                while stack and stack[-1].isdigit():
                    cur_num = stack.pop() + cur_num
                cur_str = int(cur_num) * cur_str
                stack.append(cur_str)
            
        return "".join(stack)
        