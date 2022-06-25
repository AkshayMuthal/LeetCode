class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [-1]*256
        ml = 0
        i = 0
        for j in range(len(s)):
            val = ord(s[j])
            i = max(i, a[val]+1)
            ml = max(ml, j-i+1)
            a[val] = j
        return ml