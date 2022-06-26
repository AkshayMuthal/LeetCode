class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1
        while True:
            sqr = n*n
            if sqr == x:
                return n
            if sqr > x:
                return n - 1
            n += 1
        