class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for i in range(n)] for j in range(m)]
        
        for i in reversed(range(n)):
            grid[m-1][i] = 1
            
        for i in reversed(range(m)):
            grid[i][n-1] = 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i!=m-1 and j!=n-1:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]
        return grid[0][0]