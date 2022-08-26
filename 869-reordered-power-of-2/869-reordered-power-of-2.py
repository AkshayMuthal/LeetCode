class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        counter = collections.Counter(str(n))
        
        for i in range(31):
            cnt = collections.Counter(str(1 << i))
            if cnt == counter:
                return True
        return False
            