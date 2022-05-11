class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0]+[1]*5
        for i in range(n):
            for k in range(1, 6):
                dp[k] += dp[k-1]
        return dp[5]