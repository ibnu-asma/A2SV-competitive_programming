# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

def solve(n:int):
    for _ in range(n):
        counts = {}
        count = 0
        length, array = int(input()), list(map(int, input().split()))
        for i, element in enumerate(array):
            diff = element - i
            if diff in counts:
                count += counts[diff]
            counts[diff] = counts.get(diff, 0) + 1
            # count = counts[diff] - 1
        # print(counts)
        print(count)



if __name__ == '__main__':
    n = int(input())
    solve(n)