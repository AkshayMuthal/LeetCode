import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        n = len(matrix)
        
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        i=1
        while i<k:
            elem = heapq.heappop(heap)
            val, r, c = elem[0], elem[1], elem[2]
            if c+1<n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
            i+=1
        
        return heapq.heappop(heap)[0]