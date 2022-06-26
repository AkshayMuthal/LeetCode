class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x
        while l<=r:
            mid = int(l + (r-l)/2)
            sqr = mid*mid
            if sqr == x:
                return mid
            elif sqr > x:
                r = mid - 1
            else:
                l = mid + 1
        return l-1