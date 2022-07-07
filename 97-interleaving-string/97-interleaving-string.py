class Solution(object):
    def interleave(self, i, j, k, s1, s2, s3, l1, l2, l3, memo):
        if i == l1 and j == l2 and k == l3:
            return True
        if k >= len(s3):
            return False
        
        if memo[i][j] != -1:
            return True if memo[i][j] == 1 else 0
        
        pick = False
        if i<l1 and s1[i] == s3[k]:
            pick = self.interleave(i+1, j, k+1, s1, s2, s3, l1, l2, l3, memo)
        if j<l2 and s2[j] == s3[k] and pick == False:
            pick = self.interleave(i, j+1, k+1, s1, s2, s3, l1, l2, l3, memo)
            
        memo[i][j] = 1 if pick else 0
        return pick
    
    
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo = [[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
        return self.interleave(0, 0, 0, s1, s2, s3, len(s1), len(s2), len(s3), memo)
