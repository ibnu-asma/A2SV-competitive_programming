# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_profit = 0
        n = len(prices)
        min_price = prices[0]
        for i in range(1, n):
            cost = prices[i] - min_price
            max_profit = max(max_profit, cost)
            min_price = min(min_price, prices[i])
        return max_profit
        