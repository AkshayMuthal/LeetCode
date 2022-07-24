class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(matrix[0])-1 
        
        while i<len(matrix) and j>=0:
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                i += 1
            else:
                j -= 1
        return False