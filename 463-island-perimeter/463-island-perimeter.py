class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rl = len(grid)
        cl = len(grid[0])
        
        perimeter = 0
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    for r, c in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                        if r<0 or r>=rl or c<0 or c>=cl or grid[r][c] == 0:
                            perimeter += 1
        return perimeter