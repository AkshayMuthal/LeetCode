class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rl, cl = len(matrix), len(matrix[0])
        for i in range(rl):
            for j in range(i, cl):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(rl):
            l, r = 0, cl-1
            while l<r:
                temp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = temp
                l+=1
                r-=1
            