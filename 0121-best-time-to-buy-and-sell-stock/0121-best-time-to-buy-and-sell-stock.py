class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        n = len(prices)
        for sell in range(1, n):
            if prices[sell] < prices[buy]:
                prices[buy] = prices[sell]
            else:
                current_profit = prices[sell] - prices[buy]
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
