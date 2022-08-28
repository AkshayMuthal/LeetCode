class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        hm = [key for key, value in sorted(hm.items(), key= lambda item: item[1], reverse=True)]
        return hm[:k]
        