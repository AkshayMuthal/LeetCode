class Solution:
    def get_longest_ss(self, text1, text2, t1, t2, l1, l2, dp):
        if t1 >= l1 or t2 >=l2:
            return 0
        
        if dp[t1][t2] != -1:
            return dp[t1][t2]
        
        if text1[t1] == text2[t2]:
            dp[t1][t2] =  1 + self.get_longest_ss(text1, text2, t1+1, t2+1, l1, l2, dp)
        else:
            skip_t1 = self.get_longest_ss(text1, text2, t1, t2+1, l1, l2, dp)
            skip_t2 = self.get_longest_ss(text1, text2, t1+1, t2, l1, l2, dp)
            dp[t1][t2] =  max(skip_t1, skip_t2)

        return dp[t1][t2]
    
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[-1 for _ in range(l2)] for _ in range(l1)]
        return self.get_longest_ss(text1, text2, 0, 0, l1, l2, dp)