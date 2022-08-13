class Solution(object):
    def lps(self, pat):
        lps = [0]*len(pat)
        i = 1
        l = 0
        while i<len(pat):
            if pat[i] == pat[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l == 0:
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l-1]
        return lps
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1
        if len(needle)==0:
            return 0
        
        lps = self.lps(needle)
        i, j = 0, 0
        
        while i<len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            if j == len(needle):
                return i-j
                # j = lps[j-1]
            elif i<len(haystack) and haystack[i]!=needle[j]:
                if j==0:
                    i+=1
                else:
                    j = lps[j-1]
        return -1