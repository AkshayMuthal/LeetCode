class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        maxc = 0
        while l<=r:
            lh, rh = height[l], height[r]
            c = min(lh, rh)*(r-l)
            maxc = max(maxc, c)
            
            if lh<rh:
                l += 1
            else:
                r -= 1
        return maxc