# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())
printed = ['#' for i in range(m)]
snake = [['.' for i in range(m)] for _ in range(n)]

count = 0
for i in range(n):
    if i % 2 == 0:
        snake[i] = printed
        continue
    
    if count % 2 == 0:
        snake[i][-1] = '#'
        count += 1
    else:
        snake[i][0] = '#'
        count += 1

for s in snake:
    print(''.join(s))




    