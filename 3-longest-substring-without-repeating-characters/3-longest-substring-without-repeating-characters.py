class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = [-1]*256
        ml = 0
        first = True
        i=0
        for j in range(len(s)):
            i = max(i, hm[ord(s[j])]+1)
            ml = max(ml, j-i+1)
            hm[ord(s[j])] = j
        return ml