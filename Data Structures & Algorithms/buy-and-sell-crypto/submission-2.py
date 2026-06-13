class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Best time to buy and sell

        maxProfit = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            profit = prices[right] - prices[left]
            maxProfit = max(profit, maxProfit)
        
        return maxProfit