class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        pal = [[False]*n for _ in range(n)]
        for i in range(n, -1, -1):
            for j in range(i, n):
                pal[i][j] = s[i] == s[j] and (j-i+1<3 or pal[i+1][j-1])
                if pal[i][j]:
                    res+=1
        return res