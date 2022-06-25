class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s not in hm:
                hm[s] = []            
            hm[s].append(strs[i])
        
        return hm.values()