class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, c = len(a)-1, len(b)-1, 0
        
        # 0+0+0 = 0, c=0
        # 1+0+0 = 1, c=0
        # 1+1+0 = 0, c=1
        # 1+1+1 = 1, c=1
        ans = ""
        
        while i>=0 and j>=0:
            va, vb = int(a[i]), int(b[j])
            if va+vb+c == 0:
                c = 0
                ans = "0" + ans
            elif va+vb+c == 1:
                c = 0
                ans = "1" + ans
            elif va+vb+c == 2:
                c = 1
                ans = "0" + ans
            elif va+vb+c == 3:
                c = 1
                ans = "1" + ans
            i-=1
            j-=1
        
        while i>=0:
            va = int(a[i])
            if va+c == 0:
                c = 0
                ans = "0" + ans
            elif va+c == 1:
                c = 0
                ans = "1" + ans
            elif va+c == 2:
                c = 1
                ans = "0" + ans
            i-=1
        
        while j>=0:
            vb = int(b[j])
            if vb+c == 0:
                c = 0
                ans = "0" + ans
            elif vb+c == 1:
                c = 0
                ans = "1" + ans
            elif vb+c == 2:
                c = 1
                ans = "0" + ans
            j-=1
        
        if c == 1:
            ans = "1" + ans
        
        return ans