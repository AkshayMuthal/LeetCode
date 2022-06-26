class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l = len(cardPoints)
        expected_len = l-k
        min_s = sys.maxint
        s = 0
        asum = 0
        
        for i in range(l):
            if i < expected_len:
                s += cardPoints[i]
                min_s = s
            else:
                s = s + cardPoints[i] - cardPoints[i-expected_len]
                min_s = min(min_s, s)
            asum += cardPoints[i]
        
        return asum-min_s
        