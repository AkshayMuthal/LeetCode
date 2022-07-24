class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, res, maxc = 0, 0, 0
        count = [0]*26
        
        for i in range(len(s)):
            count[ord(s[i])-ord('A')] += 1
            maxc = max(maxc, count[ord(s[i])-ord('A')])
            if i-start-maxc+1  > k:
                count[ord(s[start])-ord('A')] -= 1
                start += 1
                for cnt in count:
                    maxc = max(maxc, cnt)
            res = max(res, i-start+1)
            # print(res, i, start)
        
        return res