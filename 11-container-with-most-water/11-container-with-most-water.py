class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        maxc = 0
        while l<=r:
            c = min(height[l], height[r])*(r-l)
            maxc = max(maxc, c)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxc