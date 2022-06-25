class Solution(object):
    def get_all_combi(self, s, ind, str_len, dp):
        if ind == str_len:
            return 1
        if s[ind] == "0":
            return 0
        if dp[ind]>0:
            return dp[ind]
            
        dnt = self.get_all_combi(s, ind+1, str_len, dp)
        
        t = 0
        val = int(s[ind:ind+2])
        
        if val>0 and val<27 and ind+2 <= str_len:
            t = self.get_all_combi(s, ind+2, str_len, dp)
        
        dp[ind] = dnt + t
        return dp[ind]
    
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)
        val = self.get_all_combi(s, 0, len(s), dp)
        return val
