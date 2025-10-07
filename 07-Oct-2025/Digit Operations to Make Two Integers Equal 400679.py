# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

import heapq

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        if len(str(n)) != len(str(m)):
            return -1
        if is_prime(n) or is_prime(m):
            return -1

        pq = [(n, n)]  
        visited = {n: n}

        while pq:
            cost, cur = heapq.heappop(pq)

            if cur == m:
                return cost

            digits = list(str(cur))

            for i in range(len(digits)):
                for d in [-1, 1]:
                    new_digit = int(digits[i]) + d
                    if 0 <= new_digit <= 9:
                        new_digits = digits[:]
                        new_digits[i] = str(new_digit)
                        new_num = int("".join(new_digits))

                        if len(str(new_num)) != len(digits):
                            continue
                        
                        if is_prime(new_num):
                            continue

                        new_cost = cost + new_num

                        if new_num not in visited or new_cost < visited[new_num]:
                            visited[new_num] = new_cost
                            heapq.heappush(pq, (new_cost, new_num))

        return -1
