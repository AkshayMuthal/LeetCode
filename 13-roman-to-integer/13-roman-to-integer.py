class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }
        prev = "I"
        value = 0
        
        for i in range(len(s)-1, -1, -1):
            if hm[s[i]] >= hm[prev]:
                value += hm[s[i]]
            else:
                value -= hm[s[i]]
            prev = s[i]
        
        return value
