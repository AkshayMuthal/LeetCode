class Solution:        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[m-1][n-1] = -1
        for i in range(n-2, -1, -1):
            obstacleGrid[m-1][i] = obstacleGrid[m-1][i+1] if obstacleGrid[m-1][i]<=0 else obstacleGrid[m-1][i]
            
        for i in range(m-2, -1, -1):
            obstacleGrid[i][n-1] = obstacleGrid[i+1][n-1] if obstacleGrid[i][n-1]<=0 else obstacleGrid[i][n-1]
                        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j]!=1:
                    obstacleGrid[i][j] += obstacleGrid[i+1][j] if obstacleGrid[i+1][j]<=0 else 0
                    obstacleGrid[i][j] += obstacleGrid[i][j+1] if obstacleGrid[i][j+1]<=0 else 0
        
        return -obstacleGrid[0][0]