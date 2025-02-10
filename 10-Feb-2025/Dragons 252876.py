# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

def solve(s:int, n: int) -> str:
    dragons = []
    for _ in range(n):
        strength ,  bouns = map(int, input().split())
        dragons.append([strength, bouns])

    dragons =  sorted(dragons,key= lambda x:x[0])
    is_winner = True
    for daragon in dragons:
        if s > daragon[0]:
            s += daragon[1]
        else:
            is_winner = False
            break
    if is_winner:
        return "YES"
    return "NO"
    

if __name__ == '__main__':
    s, n = map(int, input().split())
    answer = solve(s, n)
    print(answer)

    