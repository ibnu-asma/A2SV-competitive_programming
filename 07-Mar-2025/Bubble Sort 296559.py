# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)  - 1
    count = 0
    while n >= 0:
        for i in range(n):
            if a[i + 1] < a[i]:
                a[i + 1], a[i] = a[i], a[i + 1]
                count += 1
        n -= 1
    print(f'Array is sorted in {count} swaps.')
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
