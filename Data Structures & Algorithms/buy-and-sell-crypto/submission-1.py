class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            else:
                profit = max(profit, prices[i] - curr)
        
        return profit

        