# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

n, given_volume, requried_volume = map(int, input().split())
arr = list(map(int, input().split()))
total_holes = sum(arr)
res = sorted(arr[1:])
count = 0
while arr[0]/total_holes * given_volume < requried_volume:
    total_holes -= res.pop()
    count += 1

print(count)