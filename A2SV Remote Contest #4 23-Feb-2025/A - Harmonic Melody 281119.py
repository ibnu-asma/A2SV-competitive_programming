# Problem: A - Harmonic Melody - https://codeforces.com/gym/590201/problem/A

melodies = int(input())
for _ in range(melodies):
    notes_num = int(input())
    notes = list(map(int, input().split()))
    is_perfect = False
    for i in range(len(notes) - 1):
        diff = abs(notes[i] - notes[i + 1])
        if diff == 5 or diff == 7:
            continue
        is_perfect = True
        print("NO")
        break
    if not is_perfect:
        print('YES')

