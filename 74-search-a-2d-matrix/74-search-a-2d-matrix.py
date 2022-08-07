class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rl, cl = len(matrix), len(matrix[0])
        i, j = 0, cl-1
        
        while i<rl and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1
            else:
                i+=1
        return False