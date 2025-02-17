# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

n = int(input())
for _ in range(n):
    zom, bul = map(int, input().split())
    health =list(map(int, input().split())) # 1 2 3
    positon = list(map(int, input().split())) # -1 2 3
    zombies = list(zip(positon, health))
    zombies.sort(key= lambda z: abs(z[0]))
    
    total_bullets = 0
    possible = True
    for pos, hea in zombies:
        distance = abs(pos)
        # Total bullets required to kill this zombie
        total_bullets += hea
        # Total bullets available in `distance` seconds
        available_bullets = bul * distance
        if total_bullets > available_bullets:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")
