class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        val = 0
        r = 0
        for i in range(len(columnTitle)-1, -1, -1):
            val += (ord(columnTitle[i])-64)*(26**r)
            r += 1
        return val