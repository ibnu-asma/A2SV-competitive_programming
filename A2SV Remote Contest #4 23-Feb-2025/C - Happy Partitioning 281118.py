# Problem: C - Happy Partitioning - https://codeforces.com/gym/590201/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()  
    
    
    zeros = [0] * (n + 1)  
    ones = [0] * (n + 1)   
    for i in range(n):
        zeros[i + 1] = zeros[i] + (a[i] == '0')
        ones[i + 1] = ones[i] + (a[i] == '1')
    
    total_zeros = zeros[n]
    total_ones = ones[n]
    
    best_i = -1
    min_dist = float('inf') 
    
    for i in range(n + 1):
        left_size = i
        left_zeros = zeros[i]
        left_req = (left_size + 1) // 2 
    
        right_size = n - i
        right_ones = total_ones - ones[i]
        right_req = (right_size + 1) // 2 
        
        if left_zeros >= left_req and right_ones >= right_req:
            dist = abs(n / 2 - i) 
            if dist < min_dist:
                min_dist = dist
                best_i = i
            elif dist == min_dist and i < best_i:
                best_i = i 
    
    print(best_i)