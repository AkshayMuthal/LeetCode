class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        sell_spot = [0]*len(prices)
        sell_spot[-1] = prices[-1]
        
        for i in range(len(prices)-2, -1, -1):
            sell_spot[i] = max(sell_spot[i+1], prices[i])
        
        for i in range(len(prices)):
            max_profit = max(max_profit, sell_spot[i] - prices[i])
        
        return max_profit