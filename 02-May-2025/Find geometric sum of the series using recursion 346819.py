# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def my(n):
    if n == 0:
        return 1
    return (1/(3**n)) + my(n - 1)


print(my(5))