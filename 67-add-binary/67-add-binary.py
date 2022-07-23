class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, c = len(a)-1, len(b)-1, 0
        ans = ""
        
        while i>=0 or j >= 0:
            s = c
            if i>=0:
                s += int(a[i])
                i -= 1
            if j>=0:
                s += int(b[j])
                j -= 1
            ans = str(s%2) + ans
            c = s/2
        
        if c == 1:
            ans = "1" + ans
        
        return ans