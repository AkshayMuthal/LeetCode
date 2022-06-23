class Solution:
    def count_min(self, coins, curr, amount, dp):
        if amount == 0:
            return 0
        if amount < 0 or curr < 0:
            return sys.maxsize
        if dp[curr][amount] != -1:
            return dp[curr][amount]
        
        donottake = self.count_min(coins, curr-1, amount, dp)
        res = donottake
        if coins[curr]<=amount:
            take = 1 + self.count_min(coins, curr, amount-coins[curr], dp)
            res = min(take, donottake)
        dp[curr][amount] = res
        return res
            
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        val = self.count_min(coins, len(coins)-1, amount, dp)
        return -1 if val == sys.maxsize else val