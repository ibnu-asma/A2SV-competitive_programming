# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n , m = map(int, input().split())
body = ['#'] * m
placeholder = [['.' for _ in range(m)] for _ in range(n)]


count = 0
for i in range(n):
    if i % 2 == 0:
        placeholder[i] = body
        continue
    if count % 2 == 0:
        placeholder[i][-1] = '#'
        count += 1
    else:
        placeholder[i][0] = "#"
        count += 1

    
[
    ['#', '#', '#', '#'],
     ['.', '.', '.', '#'],
      ['#', '#', '#', '#']
]

for line in placeholder:
    print(''.join(line))

