# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

n , x0 = map(int, input().split())
segments = []
for _ in range(n):
    ai, bi = map(int, input().split())
    segments.append((ai, bi))
left = 0
right = 1000
for ai, bi in segments:
    left_segment = min(ai, bi)
    right_segment = max(ai, bi)
    left = max(left, left_segment)
    right = min(right, right_segment)

if left > right:
    print(-1)
else: 
    if x0 < left:
        distance = left - x0
    elif x0 > right:
        distance = x0 - right
    else:
        distance = 0
    print(distance)