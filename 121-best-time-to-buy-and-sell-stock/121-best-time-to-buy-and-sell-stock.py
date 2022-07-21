class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        max_curr = 0
        
        for i in range(1, len(prices)):
            max_curr = max(0, max_curr + prices[i]-prices[i-1])
            max_profit = max(max_profit, max_curr)
        
        return max_profit