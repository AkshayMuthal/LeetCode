class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minlen = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(row+1):
                minlen[col] = min(minlen[col], minlen[col+1]) + triangle[row][col]
        return minlen[0]