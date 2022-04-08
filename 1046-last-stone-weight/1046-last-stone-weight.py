import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        hq = [-x for x in stones]
        heapq.heapify(hq)
        
        while len(hq)>1:
            heapq.heappush(hq, heapq.heappop(hq) - heapq.heappop(hq))
        return -hq[0]