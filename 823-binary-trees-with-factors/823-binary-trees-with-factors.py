class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hm = {}
        arr.sort()
        bt = 0
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                rem = arr[j]%arr[i]
                ques = arr[j]/arr[i]
                if rem == 0 and ques in arr:
                    hm[arr[j]] = hm.get(arr[j], []) + [(arr[i], ques)]
        
        hm = OrderedDict(sorted(hm.items()))
#         for k, v in hm.items():
#             print(k, v)
        
        hm2 = {}
        for k, v in hm.items():
            for pair in v:
                p1, p2 = hm2.get(pair[0], 0), hm2.get(pair[1], 0)
                hm2[k] = hm2.get(k, 0) + p1 + p2 + p1*p2 + 1
            bt += hm2[k]
        return (bt+len(arr))%1000000007