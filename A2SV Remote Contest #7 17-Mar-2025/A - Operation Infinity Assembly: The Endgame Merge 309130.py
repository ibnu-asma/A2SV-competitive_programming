# Problem: A - Operation Infinity Assembly: The Endgame Merge - https://codeforces.com/gym/596004/problem/A

def solve_test_case():
    n, m, k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())  
    
    i = 0  
    j = 0  
    
    result = []
    consecutive_count = 0  
    last_used = None
    
    while i < n and j < m:
        if consecutive_count < k and (j >= m or a[i] < b[j]):
            result.append(a[i])
            i += 1
            if last_used == 'a':
                consecutive_count += 1
            else:
                consecutive_count = 1
                last_used = 'a'
        elif consecutive_count < k and (i >= n or b[j] < a[i]):
            result.append(b[j])
            j += 1
            if last_used == 'b':
                consecutive_count += 1
            else:
                consecutive_count = 1
                last_used = 'b'
        elif last_used == 'a':
            result.append(b[j])
            j += 1
            consecutive_count = 1
            last_used = 'b'
        else:
            result.append(a[i])
            i += 1
            consecutive_count = 1
            last_used = 'a'
    
    return ''.join(result)


t = int(input())
for _ in range(t):
    print(solve_test_case())