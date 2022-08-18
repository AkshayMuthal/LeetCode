class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = collections.Counter(arr)
        req_len = len(arr)/2
        occurances = 0
        cnt = 0
        
        for pair in count.most_common():
            if occurances>=req_len:
                return cnt
            occurances += pair[1]
            cnt += 1
        
        return cnt