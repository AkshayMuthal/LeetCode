class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rl = len(matrix)
        self.cl = len(matrix[0])
        self.dp = [[0 for _ in range(self.cl+1)] for _ in range(self.rl+1)]
        
        for r in range(self.rl):
            for c in range(self.cl):
                self.dp[r+1][c+1] = self.dp[r+1][c] + self.dp[r][c+1] + matrix[r][c] - self.dp[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg