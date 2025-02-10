# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

def solve(n:int):
    
    for _ in range(n):
        word = input()
        query_length = int(input())   
        count =  word.count("1100")
        current_string = list(word)
        for _ in range(query_length):
            place, value = map(int, input().split())
            place = place - 1
            start = max(0, place - 3)
            end = place + 4
            sub_string_before = "".join(current_string[start: end]).count("1100")
            current_string[place] = str(value)
            sub_string_after = "".join(current_string[start: end]).count("1100")
            count += sub_string_after - sub_string_before 
            print("YES") if count  else print("NO")


    

if __name__ == '__main__':
    n = int(input()) 
    solve(n)
