class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rl, cl = len(matrix), len(matrix[0])
        l, h = 0, (rl*cl)-1
        
        while l<=h:
            mid = l + (h-l)//2
            num = matrix[mid/cl][mid%cl]
            if num == target:
                return True
            elif num > target:
                h = mid-1
            else:
                l = mid+1
        return False