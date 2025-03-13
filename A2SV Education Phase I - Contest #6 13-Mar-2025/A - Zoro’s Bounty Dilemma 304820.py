# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

n = int(input())
for _ in range(n):
    data = input()
    if '<' in data and '>' in data:
        print('?')
    elif '<' in data:
        print('<')
    elif '>' in data:
        print('>')
    else:
        print('=')
        