class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = len(coins)
        dp = [[amount+1 for _ in range(l+1)] for _ in range(amount+1)]
        
        for i in range(amount+1):
            for j in range(l+1):
                if i ==0 or j ==0:
                    dp[i][j] = 0 if i==0 else sys.maxsize
        
        
        for i in range(1, amount+1):
            for j in range(1, l+1):
                dp[i][j] = dp[i][j-1]
                if coins[j-1]<=i:
                    dp[i][j] = min(dp[i][j], 1+dp[i-coins[j-1]][j])
        
        return dp[amount][l] if dp[amount][l] != sys.maxsize else -1