# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            duplicate = set()
            for num in row:
                if num == '.':
                    continue
                if num in duplicate:
                    return False
                duplicate.add(num)
            
        for i in range(9):
            duplicate = set()
            for j in range(9):
                cur = board[j][i]
                if cur  == '.':
                    continue
                if cur in duplicate:
                    return False
                duplicate.add(cur)

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    col = (square % 3)*3 + j
                    row = (square // 3)*3 + i
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
            


            
        