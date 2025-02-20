# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
friends = [input() for _ in range(n)]
has_conversation = set()
check_list = []
for friend in reversed(friends):
    if friend in has_conversation:
        continue
    print(friend)
    has_conversation.add(friend)

