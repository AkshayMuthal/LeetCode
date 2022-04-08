class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        l, r = 0, len(stones)-1
        
        while r>0:
            stones[l:(r+1)] = sorted(stones[l:(r+1)])
            print(stones[l:(r+1)])

            if stones[r]==stones[r-1]:
                r-=1
            else:
                elem = stones[r]-stones[r-1]
                stones[r-1]=elem
            r-=1
        if r<0:
            return 0
        return stones[0]