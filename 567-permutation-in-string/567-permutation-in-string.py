class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if l1>l2:
            return False
        
        A = [ord(c)-ord('a') for c in s1]
        B = [ord(c)-ord('a') for c in s2]
        
        target = [0]*26
        for i in A:
            target[i]+=1
        
        window = [0]*26
        for i, x in enumerate(B):
            window[x]+=1
            if i>=l1:
                window[B[i-l1]]-=1
            if window==target:
                return True
        return False
        