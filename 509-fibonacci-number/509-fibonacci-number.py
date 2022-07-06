class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        
        curr, p, gp, i = 0, 1, 0, 2
        
        while i <= n:
            curr = p + gp
            gp = p
            p = curr
            i += 1
        return curr
        