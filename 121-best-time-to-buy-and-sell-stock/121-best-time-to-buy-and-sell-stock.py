class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        minl = prices[0]
        
        for i in prices:
            minl = min(minl, i)
            max_profit = max(max_profit, i-minl)
        
        return max_profit