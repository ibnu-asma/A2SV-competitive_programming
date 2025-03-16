# Problem: Books - https://codeforces.com/contest/279/problem/B

def max_books(n, t, a):
    left = 0
    current_time = 0
    max_books_count = 0
    
    for right in range(n):
        current_time += a[right]
        
        while current_time > t:
            current_time -= a[left]
            left += 1
            
        max_books_count = max(max_books_count, right - left + 1)
    
    return max_books_count

n, t = map(int, input().split())
a = list(map(int, input().split()))

result = max_books(n, t, a)
print(result)

