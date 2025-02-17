# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input()
n = int(input())
words = [input().strip() for _ in range(n)]

if password in words:
    print("YES")
    exit()
is_done = False
for i in range(n):
    for j in range(n):
         if words[i][1] + words[j][0] == password or words[j][1] + words[i][0] == password:
            is_done = True
            print('YES')
            break
    if is_done:
        break
if not is_done:
    print('NO')
