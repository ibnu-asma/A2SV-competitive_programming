# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
matrix = []
for  _ in range(n):
    row = list(map(int, input().split()))
    cur_row = [0] * n   
    for i in range(1, row[0] + 1):
        cur_row[row[i]- 1] = 1
    print(*cur_row)

    