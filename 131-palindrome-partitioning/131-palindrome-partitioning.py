class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(start, s, dp, ans, cl):
            """
            :type start:int
            :type s: str
            :type dp: List[bool]
            :type ans: List[List[str]]
            :type cl: List[str]
            """
            if start==len(s):
                ans.append(cl)
            
            for end in range(start, len(s)):
                if s[start] == s[end] and (end-start<=2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    dfs(end+1, s, dp, ans, cl+[s[start:end+1]])
        
        
        dp = [[False]*len(s) for _ in range(len(s))]
        ans = []
        dfs(0, s, dp, ans, [])
        return ans