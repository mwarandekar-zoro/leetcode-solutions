class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices.copy()
        for i in range (n):
            for j in range (i+1,n):
                if prices[j] <= prices[i]:
                    ans[i] -= prices[j]
                    break
        return ans