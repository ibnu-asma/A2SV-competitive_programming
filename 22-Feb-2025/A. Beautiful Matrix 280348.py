# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

x = 0
y = 0
for _ in range(5):
    current_list = list(map(int, input().split()))
    if 1 in current_list:
        y = current_list.index(1)
        break
    x += 1

print(abs(2 - x ) + abs(2 - y))


