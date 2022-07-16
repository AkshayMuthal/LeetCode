class Solution(object):
    def dfs(self, i, j ,m, n, mat, N):
        if i<0 or j<0 or i>=m or j>=n:
            return 1
        if N == 0:
            return 0
        if mat[i][j][N] != -1:
            return mat[i][j][N]
        
        path = 0
        for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            path += (self.dfs(r, c ,m, n, mat, N-1))%self.modulo
        
        mat[i][j][N] = path%self.modulo
        return mat[i][j][N]
        
    
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        self.modulo = 1000000007
        mat = [[[-1]*(maxMove+1) for _ in range(n)] for _ in range(m)]
        
        return self.dfs(startRow, startColumn, m, n, mat, maxMove)