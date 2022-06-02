class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rl = len(matrix)
        cl = len(matrix[0])
        
        new_mat = [[0 for _ in range(rl)] for _ in range(cl)]
        for i in range(rl):
            for j in range(cl):
                new_mat[j][i] = matrix[i][j]
        return new_mat
