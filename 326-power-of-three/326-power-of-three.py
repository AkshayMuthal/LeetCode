import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        val = (math.log10(abs(n))/math.log10(3))
        if n<0 or val%1!=0:
            return False
        return True