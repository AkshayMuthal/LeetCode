import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 or (math.log10(abs(n))/math.log10(3))%1!=0:
            return False
        return True