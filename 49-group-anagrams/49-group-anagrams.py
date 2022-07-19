class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = defaultdict()
        for i in strs:
            s = ''.join(sorted(i))
            hm[s] = hm.get(s, []) + [i]
        return hm.values()