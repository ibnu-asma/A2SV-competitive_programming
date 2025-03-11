# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

def solve():
    n, op = map(int, input().split())
    nums = list(map(int, input().split()))
    current_max = max(nums)
    res = [0]*op
    
    for i in range(op):
        c, l, r = input().split()
        l, r = int(l), int(r)
        if l <= current_max <= r:
            if c == '+':
                current_max += 1
                res[i] = current_max
            else:
                current_max -= 1
                res[i] = current_max
            continue
        res[i] = current_max
    print(*res)




if __name__ == '__main__':
    for _ in range(int(input())):
        solve()