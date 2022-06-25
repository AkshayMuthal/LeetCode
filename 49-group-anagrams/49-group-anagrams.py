class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for i in range(len(strs)):
            char = [0]*26
            for j in strs[i]:
                char[ord(j)-97] += 1
            s = ""
            for j in range(26):
                s = s + "#" + str(char[j])
            if s not in hm:
                hm[s] = []            
            hm[s].append(strs[i])
        
        return hm.values()