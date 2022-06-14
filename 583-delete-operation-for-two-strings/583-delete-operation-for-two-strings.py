class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        return m+n - 2*self.lcs(word1, word2, m, n, memo)

    def lcs(self, s1, s2, m , n, memo):
        if m == 0 or n == 0:
            return 0
        elif memo[m][n]>0:
            return memo[m][n]
        elif s1[m-1] == s2[n-1]:
            memo[m][n] = 1 + self.lcs(s1, s2, m-1, n-1, memo)
        else:
            memo[m][n] = max(self.lcs(s1, s2, m-1, n, memo), self.lcs(s1, s2, m, n-1, memo))
        return memo[m][n]