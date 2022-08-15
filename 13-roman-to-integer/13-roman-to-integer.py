class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {
          "I": [0, 1],
          "V": [1, 5],
          "X": [2, 10],
          "L": [3, 50],
          "C": [4, 100],
          "D": [5, 500],
          "M": [6, 1000]
        }
        prev = "I"
        value = 0
        
        for i in range(len(s)-1, -1, -1):
            if hm[s[i]][0] >= hm[prev][0]:
                value += hm[s[i]][1]
            else:
                value -= hm[s[i]][1]
            prev = s[i]
        
        return value
