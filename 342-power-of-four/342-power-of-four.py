class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0 and n%2!=0:
            return False
        check = 1
        while n:
            if check and n==1:
                return True
            if n%2!=0:
                return False
            check ^= 1
            n >>= 1
        return False