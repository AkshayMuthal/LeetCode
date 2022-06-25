class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def get_str(s):
            char = [0]*26
            for i in s:
                char[ord(i)-97] += 1
            
            ans = ""
            for i in range(26):
                ans = ans + "#" + str(char[i])
            return ans
        
        hm = {}
        
        for i in range(len(strs)):
            s = get_str(strs[i])
            if s not in hm:
                hm[s] = []
            hm[s].append(strs[i])
        
        return hm.values()