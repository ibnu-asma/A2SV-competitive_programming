# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
                    continue
            elif log == './':
                pass
            else:
                stack.append(log)

        print(stack)
        return len(stack)