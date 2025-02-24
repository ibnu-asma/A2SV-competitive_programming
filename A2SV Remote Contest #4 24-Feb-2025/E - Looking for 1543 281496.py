# Problem: E - Looking for 1543 - https://codeforces.com/gym/590201/problem/E

def get_layer_sequence(grid, n, m, k):
    if n <= 0 or m <= 0:
        return ""
    seq = []
    for j in range(k, m - k):
        seq.append(grid[k][j])
    for i in range(k + 1, n - k):
        seq.append(grid[i][m - 1 - k])
    if n - k - 1 > k:
        for j in range(m - 1 - k - 1, k - 1, -1):
            seq.append(grid[n - 1 - k][j])
    if m - k - 1 > k:
        for i in range(n - 1 - k - 1, k, -1):
            seq.append(grid[i][k])
    return "".join(seq)

def count_1543(s):
    if len(s) < 4:
        return 0
    s_extended = s + s[:3]
    count = 0
    target = "1543"
    for i in range(len(s)):
        if s_extended[i:i+4] == target:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    
    total_count = 0
    k = 0
    while True:
        curr_n = n - 2 * k
        curr_m = m - 2 * k
        if curr_n <= 0 or curr_m <= 0:
            break
        seq = get_layer_sequence(grid, n, m, k)
        total_count += count_1543(seq)
        k += 1
    
    print(total_count)