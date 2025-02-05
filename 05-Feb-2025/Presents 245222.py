# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
accepted_from = list(map(int, input().split()))

result = [0] * n 
for i in range(len(accepted_from)):
    result[accepted_from[i] - 1] = i + 1

print(*result)
