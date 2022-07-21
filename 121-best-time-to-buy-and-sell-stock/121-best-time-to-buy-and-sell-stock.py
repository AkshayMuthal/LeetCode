class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        minl = prices[0]
        
        for i in range(1, len(prices)):
            minl = min(minl, prices[i])
            max_profit = max(max_profit, prices[i]-minl)
        
        return max_profit