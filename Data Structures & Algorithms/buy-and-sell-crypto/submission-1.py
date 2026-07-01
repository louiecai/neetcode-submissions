class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        maxProfit = 0
        low = prices[0]
        for price in prices[1:]:
            maxProfit = max(price - low, maxProfit)
            low = min(low, price)
        return maxProfit
