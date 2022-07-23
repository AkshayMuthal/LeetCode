class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        # 6
        # 2 2 2
        cnt, i, j = 0, 0, 0
        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                cnt += 1
                i += 1
            j += 1
        return cnt
                