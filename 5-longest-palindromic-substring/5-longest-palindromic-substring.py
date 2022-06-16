class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        res = ""
        
        def helper(s, l, r):
            while l>=0 and r<size and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(size):
            temp = helper(s, i, i)
            if len(res)<len(temp):
                res = temp
            
            temp = helper(s, i, i+1)
            if len(res)<len(temp):
                res = temp
            
        return res