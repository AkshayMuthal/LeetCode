class Solution:    
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0]*len(s)
        
        def rec(ind, s, cnt, dp):
            if ind == len(s):
                cnt += 1
                return cnt
            if ind > len(s) or s[ind] == "0":
                return cnt
            if dp[ind]!= 0 :
                cnt += dp[ind]
                return cnt
            
            cnt = rec(ind+1, s, cnt, dp)
            if ind+2 <= len(s) and int(s[ind:ind+2])<27:
                cnt = rec(ind+2, s, cnt, dp)
            
            dp[ind] = cnt
            return cnt

        cnt = 0
        cnt = rec(0, s, cnt, dp)
        return cnt