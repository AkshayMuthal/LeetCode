class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rl, cl = len(grid), len(grid[0])
        q = deque()
        cnt = 0
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q:
            cnt += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1),]:
                    if i>=0 and i<rl and j>=0 and j<cl and grid[i][j] == 1:
                        grid[i][j] = 2
                        q.append((i, j))
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    return -1
        return cnt-1 if cnt-1>=0 else 0
