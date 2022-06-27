class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        maxe = 0
        for i in n:
            maxe = max(maxe, int(i))
        return maxe