class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        for k,v in hm.items():
            if v==1:
                return k