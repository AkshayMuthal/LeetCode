class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def gen_num(n):
            val = 0
            while n:
                rem = n%10
                n /= 10
                val += rem**2
            return val
        
        hs = set()
        while n!=1 and n not in hs:
            hs.add(n)
            n = gen_num(n)
            
        return True if n==1 else False