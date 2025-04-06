# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

# Read the number of cards
n = int(input())
# Read the card values into a list
cards = list(map(int, input().split()))

# Initialize scores
sereja_score = 0
dima_score = 0

# Two pointers for left and right ends
left = 0
right = n - 1

# Turn tracker: True for Sereja, False for Dima
sereja_turn = True

# Continue until pointers meet or cross
while left <= right:
    # Choose the larger card from either end
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    
    # Assign the chosen card to the current player
    if sereja_turn:
        sereja_score += chosen
    else:
        dima_score += chosen
    
    # Switch turns
    sereja_turn = not sereja_turn

# Output the final scores
print(sereja_score, dima_score)