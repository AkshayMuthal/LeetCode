class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for r in range(m+1):
            for c in range(n+1):
                if r == 0 or c == 0:
                    continue
                elif word1[r-1] == word2[c-1]:
                    memo[r][c] = 1+memo[r-1][c-1]
                else:
                    memo[r][c] = max(memo[r-1][c], memo[r][c-1])
        return m+n - 2*memo[m][n]
