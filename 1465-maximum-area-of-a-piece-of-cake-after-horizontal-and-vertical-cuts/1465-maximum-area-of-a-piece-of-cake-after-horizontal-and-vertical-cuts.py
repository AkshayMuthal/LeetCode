class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()

        maxr = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            maxr = max(maxr, horizontalCuts[i] - horizontalCuts[i-1])
        maxr = max(maxr, h - horizontalCuts[-1])
        
        maxc = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            maxc = max(maxc, verticalCuts[i] - verticalCuts[i-1])
        maxc = max(maxc, w - verticalCuts[-1])
        
        return (maxr*maxc)%1000000007
        