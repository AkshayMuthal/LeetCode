class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bs(arr, l, r, target):
            while l<=r:
                mid = l + (r-l)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        h = len(matrix[0])
        for i in range(len(matrix)):
            if bs(matrix[i], 0, h-1, target):
                return True
        return False