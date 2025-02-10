# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

def solve(n:int, t:int):
    number  = int("9" * n)
    min_number = 10** (n -1)
    while number >= min_number:
        if number % t == 0:
            return number
        number -= 1
    return -1
            
    
if __name__ == '__main__':
    n, t = map(int, input().split())
    result = solve(n, t)
    print(result)