class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rl = len(grid)
        cl = len(grid[0])
        
        def get_perimeter(i, j):
            # print(i, j)
            if i<0 or i>=rl or j<0 or j>=cl or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            
            grid[i][j] = -1
            perimeter = 0 
            for r, c in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                perimeter += get_perimeter(r, c)
            
            # print("perimeter: ", perimeter)
            return perimeter
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    return get_perimeter(i, j)