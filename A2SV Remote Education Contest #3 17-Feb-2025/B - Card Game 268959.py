# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

n = int(input())
players = n // 2
sequences = list(map(int, input().split()))
target = sum(sequences) // players
is_paired = [False]*n


for i, seq in enumerate(sequences):
    if is_paired[i]:
        continue
    for j in range(i + 1, n):
        if not is_paired[j] and sequences[j] + sequences[i] == target:
            print(i + 1, j + 1)
            is_paired[i] = True
            is_paired[j] = True
            break
        

    
    

    


