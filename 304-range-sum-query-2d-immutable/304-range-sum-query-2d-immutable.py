class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rl = len(matrix)
        self.cl = len(matrix[0])
        for i in range(self.rl):
            for j in range(1, self.cl):
                matrix[i][j] += matrix[i][j-1]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            sum += self.matrix[i][col2]-self.matrix[i][col1-1] if col1!=0 else self.matrix[i][col2]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg