class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, res, maxc = 0, 0, 0
        count = {}
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxc = max(maxc, count[s[right]])

            while (right-left+1)-maxc  > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res