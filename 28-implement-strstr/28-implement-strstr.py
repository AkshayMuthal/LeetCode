class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)>len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack)):
            found = True
            for j in range(len(needle)):
                if i+j>=len(haystack) or haystack[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1
        