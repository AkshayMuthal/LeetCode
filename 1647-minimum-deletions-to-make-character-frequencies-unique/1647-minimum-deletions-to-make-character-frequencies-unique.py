class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hm = defaultdict()
        for i in s:
            hm[i] = hm.get(i, 0)+1
        
        values = sorted(hm.values())
        steps = 0
        for i in range(len(values)-2, -1, -1):
            if values[i+1] == 0:
                steps += values[i]
                values[i] = 0
            elif values[i] >= values[i+1]:
                diff = values[i]-values[i+1]+1
                values[i] -= diff
                steps += diff
        return steps
        