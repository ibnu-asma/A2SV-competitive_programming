# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C


def solve(n:int, encoded:str):
    original = []
    for letter in reversed(encoded):
        length = len(original)
        pos = length // 2
        original.insert(pos, letter)
    return ''.join(original)


                 
                 
if __name__ == '__main__':
    n = int(input())
    encoded_word = input()
    decoded = solve(n, encoded_word)
    print(decoded)
  