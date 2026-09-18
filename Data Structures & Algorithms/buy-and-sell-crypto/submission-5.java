class Solution {
    // Dynamic Programming

    public int maxProfit(int[] prices) {
        int minBuy = prices[0];
        int maxP = 0;

        for(int sell : prices){
            int profit = sell - minBuy;
            maxP = Math.max(profit, maxP);

            minBuy = Math.min(sell, minBuy);
        }

        return maxP;
    }
}
