class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*(len(s)) for _ in range(len(s))]
        maxs = 0
        ns, ne = 0, 0
        
        for start in range(len(s)-1, -1, -1):
            for end in range(start, len(s)):
                if s[start] == s[end] and (end-start<=2 or dp[start+1][end-1]):
                    dp[start][end] = 1
                    if end-start+1>maxs:
                        ns = start
                        ne = end
                        maxs = end-start+1
        
        return s[ns:ne+1]