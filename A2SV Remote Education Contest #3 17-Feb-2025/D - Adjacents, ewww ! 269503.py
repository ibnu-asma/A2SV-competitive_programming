# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

t = int(input())

for _ in range(t):
    matrx_size = int(input())
    if matrx_size == 2:
        print(-1)
    else:
        items = [t for t in range(1, matrx_size**2 + 1)]
        count = 0
        for i in range(0,len(items), 2):
            count += 1
            print(items[i], " ", end="")
            if i > 0 and count % matrx_size == 0:
                print()
            if len(items) == 1:
                print()
        for i in range(1,len(items), 2):
            print(items[i], " ", end= "")
            count += 1
            if count % matrx_size == 0:
                print()



    