class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        def get_sorted_array(r, c, rl, cl, mat):
            arr = []
            while c<cl and r<rl:
                arr.append(mat[r][c])
                r += 1
                c += 1
            
            arr.sort()
            return arr
        
        def replace_array(r, c, rl, cl, mat, arr):
            ind = 0
            while c<cl and r<rl:
                mat[r][c] = arr[ind]
                r += 1
                c += 1
                ind += 1
        
        rl, cl = len(mat), len(mat[0])
        
        for i in range(cl-1, -1, -1):
            r, c = 0, i
            sorted_array = get_sorted_array(r, c, rl, cl, mat)
            replace_array(0, i, rl, cl, mat, sorted_array)
                
        for i in range(1, rl):
            r, c = i, 0
            sorted_array = get_sorted_array(r, c, rl, cl, mat)
            replace_array(i, 0, rl, cl, mat, sorted_array)

        return mat