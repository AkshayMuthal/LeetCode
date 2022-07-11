class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp0, dp1 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            dp2 = cost[i] + min(dp1, dp0)
            dp0 = dp1
            dp1 = dp2
        
        return min(dp0, dp1)