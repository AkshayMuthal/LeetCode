class Solution:
    def cover_island(self, grid, r, c, rl, cl):
        if grid[r][c] == "-1" or grid[r][c] == "0":
            return
        
        grid[r][c] = "-1"
        for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if i>=0 and i<rl and j>=0 and j<cl:
                self.cover_island(grid, i, j, rl, cl)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        island_count = 0
        
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == "1":
                    # print(r, c)
                    island_count += 1
                    self.cover_island(grid, r, c, rl, cl)
        
                    # for r in range(rl):
                    #     print(grid[r])
                    # print()

        return island_count