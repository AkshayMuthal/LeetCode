class Solution(object):
    def count_island(self, i, j, r, c, grid):
        if grid[i][j] == -1 or grid[i][j] == 0:
            return 0
        
        grid[i][j] = -1
        count = 1
        
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if ni >=0 and ni <r and nj>=0 and nj<c:
                count += self.count_island(ni, nj, r, c, grid)
        return count
                
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        max_count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    max_count = max(self.count_island(i,j,r,c,grid), max_count)
                
        return max_count     