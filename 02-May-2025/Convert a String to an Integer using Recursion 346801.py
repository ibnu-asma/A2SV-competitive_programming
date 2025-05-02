# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def str_to_int(s, i, n):
    if i == n:
        return 0
    digit = int(s[i])
    return digit * (10** (n - i - 1)) + str_to_int(s, i + 1, n)

    
    


print(type(str_to_int('112', 0, 3)))
    