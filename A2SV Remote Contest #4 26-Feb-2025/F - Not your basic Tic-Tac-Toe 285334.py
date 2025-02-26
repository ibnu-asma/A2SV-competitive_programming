# Problem: F - Not your basic Tic-Tac-Toe - https://codeforces.com/gym/590201/problem/F


grid = []
for i in range(11):
    line = input().strip()
    if line:
        grid.append(line)


x, y = map(int, input().split())
x -= 1
y -= 1

board = []
for i in range(9):
    row = grid[i][0:3] + grid[i][4:7] + grid[i][8:11]
    board.append(list(row))

small_x = x // 3
small_y = y // 3
local_x = x % 3
local_y = y % 3

target_small_x = local_x
target_small_y = local_y

target_start_row = target_small_x * 3
target_start_col = target_small_y * 3
has_empty = False
for i in range(3):
    for j in range(3):
        if board[target_start_row + i][target_start_col + j] == '.':
            has_empty = True
            break
    if has_empty:
        break

if has_empty:
    for i in range(3):
        for j in range(3):
            r = target_start_row + i
            c = target_start_col + j
            if board[r][c] == '.':
                board[r][c] = '!'
else:
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                board[i][j] = '!'

for i in range(9):
    row = (
        ''.join(board[i][0:3]) + ' ' +
        ''.join(board[i][3:6]) + ' ' +
        ''.join(board[i][6:9])
    )
    print(row)
    if i == 2 or i == 5:
        print()