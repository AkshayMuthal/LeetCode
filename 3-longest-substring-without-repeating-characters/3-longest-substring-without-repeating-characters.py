class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [-1]*256
        l = 0
        ml = 0
        i = 0
        for j in range(len(s)):
            val = ord(s[j])
            if a[val] == -1:
                l += 1
            else:
                i = max(i, a[val])
                l = j - i
            ml = max(ml, l)
            a[val] = j
        return ml