class Solution:    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = deque()
        queue.append((0, 0, 1))
        # grid[0][0] = 1
        
        
        # while len(queue)>0:
        #     i, j, k = queue.pop()
        #     if i==n-1 and j==n-1:
        #         return k
        #     for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
        #         if 0<=x<n and 0<=y<n and grid[x][y] == 0:
        #             grid[x][y] = 1
        #             queue.appendleft((x, y, k+1))
        # return -1

    
        while len(queue)>0:
            i, j, k = queue.pop()
            if i<0 or i>=n or j<0 or j>=n or grid[i][j] == 1:
                continue
                
            if i==n-1 and j==n-1:
                return k
            
            grid[i][j] = 1
            
            queue.appendleft((i-1, j-1, k+1))
            queue.appendleft((i-1, j, k+1))
            queue.appendleft((i-1, j+1, k+1))
            queue.appendleft((i, j-1, k+1))
            queue.appendleft((i, j+1, k+1))
            queue.appendleft((i+1, j-1, k+1))
            queue.appendleft((i+1, j, k+1))
            queue.appendleft((i+1, j+1, k+1))
        
        return -1