class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = [-1]*256
        ml = 0
        last = 0
        for i in range(len(s)):
            val = char[ord(s[i])]
            last = max(last, val+1)
            ml = max(ml, i-last+1)
            char[ord(s[i])] = i
        return ml