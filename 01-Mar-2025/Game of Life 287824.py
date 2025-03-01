# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def gameOfLife(board):
            if not board or not board[0]:
                return
        
        # Get dimensions of the board
        m, n = len(board), len(board[0])
        
        # Helper function to count live neighbors
        def count_neighbors(row, col):
            count = 0
            # Check all 8 directions
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:  # Skip the cell itself
                        continue
                    r, c = row + i, col + j
                    # Check if within bounds and if neighbor is live (1 or -1)
                    if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                        count += 1
            return count
        
        # Step 1: Mark cells with temporary states
        # Use -1 for live -> dead, 2 for dead -> live
        for i in range(m):
            for j in range(n):
                neighbors = count_neighbors(i, j)
                if board[i][j] == 1:  # Live cell
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = -1  # Dies (under/over-population)
                else:  # Dead cell
                    if neighbors == 3:
                        board[i][j] = 2  # Becomes alive (reproduction)
        
        # Step 2: Update the board to final states (0 or 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0  # Live -> dead
                elif board[i][j] == 2:
                    board[i][j] = 1  # Dead -> live

        # Example usage
        board = [[0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]]
        gameOfLife(board)

        # Print the updated board
        for row in board:
            print(row)
                