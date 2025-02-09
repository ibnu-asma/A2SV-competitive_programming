# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(n:int) ->int:
    if n < 6:
        return 0
        
    
    count = 0
    for i in range(6, n + 1):
        # is_prime = True
        current_count = 0
        for num in range(i + 1):
            divider  = num
            if is_prime(divider):
                if i % divider == 0:
                    current_count += 1
        if current_count == 2:
            count += 1
        current_count = 0

    return count 
        







if __name__ == '__main__':
    n = int(input())
    print(solve(n))