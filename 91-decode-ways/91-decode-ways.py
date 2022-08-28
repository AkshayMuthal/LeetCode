class Solution:    
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, len(s)+1):
            first = int(s[i-1:i])
            sec = int(s[i-2:i])
            
            if 0<first<=9:
                dp[i] += dp[i-1]
            if 10<=sec<27:
                dp[i] += dp[i-2]
        
        return dp[len(s)]