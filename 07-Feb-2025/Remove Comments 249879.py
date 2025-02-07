# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        is_block_comment = False
        current_line = ""  # Accumulate the current line across source lines

        for line in source:
            i = 0
            while i < len(line):
                if is_block_comment:
                    if line[i:i+2] == "*/":
                        is_block_comment = False
                        i += 2
                    else:
                        i += 1
                elif line[i:i+2] == "/*":
                    is_block_comment = True
                    i += 2
                elif line[i:i+2] == "//":
                    break  # Ignore the rest of the line
                else:
                    current_line += line[i]
                    i += 1

            if not is_block_comment and current_line:  # Check only when NOT in block comment
                result.append(current_line)
                current_line = "" # Reset for the next line

        return result