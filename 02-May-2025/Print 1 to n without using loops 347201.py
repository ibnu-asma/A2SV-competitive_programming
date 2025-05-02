# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/


def nums(num):
    if num > 0:
        nums(num - 1)
        print(num, end = ' ')
    