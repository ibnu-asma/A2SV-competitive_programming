# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    consonant_substring = 0
    vowels_substring = 0
    vowls = {'A','E','I','O', 'U'}
    length = len(string)
    for i, c in enumerate(string):
        if c in vowls:
            vowels_substring += length - i
        else:
            consonant_substring += length - i
    
    
    if consonant_substring > vowels_substring:
        print("Stuart", consonant_substring)
    elif consonant_substring < vowels_substring:
        print("Kevin", vowels_substring)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)