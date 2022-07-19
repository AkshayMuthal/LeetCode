class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        for i in nums:
            hm[i] = hm.get(i, 0)+1
        
        freq = {}
        for key, v in hm.items():
            freq[v] = freq.get(v, []) + [key]
        
        ans = []
        for i in range(len(nums), 0, -1):
            if i in freq:
                for key in freq[i]:
                    ans.append(key)

        return ans[:k]