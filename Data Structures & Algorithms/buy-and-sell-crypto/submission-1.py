class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        left, right = 0, 1
        maxProfit = prices[right] - prices[left]

        while right < len(prices):
            maxProfit = max(maxProfit, prices[right] - prices[left])

            if(prices[right] < prices[left]):
                left = right
            
            right = right + 1
        
        return maxProfit if maxProfit > 0 else 0
        