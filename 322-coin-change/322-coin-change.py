class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = len(coins)
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        coins.sort()
        
        for amt in range(1, amount+1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1+dp[amt-coin])
                else:
                    break
        
        return dp[amount] if dp[amount] != amount+1 else -1