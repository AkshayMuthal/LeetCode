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

        hl, vl = len(horizontalCuts), len(verticalCuts)

        maxr = horizontalCuts[0]
        for i in range(1, hl):
            maxr = max(maxr, horizontalCuts[i] - horizontalCuts[i-1])

        maxr = max(maxr, h - horizontalCuts[-1])
        
        maxc = verticalCuts[0]
        for i in range(1, vl):
            maxc = max(maxc, verticalCuts[i] - verticalCuts[i-1])
        maxc = max(maxc, w - verticalCuts[-1])
        
        return (maxr*maxc)%1000000007
        