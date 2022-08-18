class Solution:
    def mincost(self, start_ind, days, n, costs, dp):
        if start_ind == len(days):
            return 0
        
        if dp[start_ind]!=-1:
            return dp[start_ind]
        
        cost_day = costs[0] + self.mincost(start_ind+1, days, n, costs, dp)
        
        i = start_ind
        while i<n and days[i] < days[start_ind]+7:
            i += 1
        cost_week = costs[1] + self.mincost(i, days, n , costs, dp)
        
        i = start_ind
        while i<n and days[i] < days[start_ind]+30:
            i += 1
        cost_month = costs[2] + self.mincost(i, days, n , costs, dp)
        
        dp[start_ind] = min(cost_day, cost_week, cost_month)
        return dp[start_ind]
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1]*len(days)
        return self.mincost(0, days, len(days), costs, dp)
