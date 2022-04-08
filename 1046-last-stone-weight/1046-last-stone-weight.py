class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        r = len(stones)-1
        
        while r>0:
            stones[:(r+1)] = sorted(stones[:(r+1)])
            print(stones[:(r+1)])

            if stones[r]==stones[r-1]:
                r-=1
            else:
                stones[r-1] = stones[r]-stones[r-1]
            r-=1
        if r<0:
            return 0
        return stones[0]