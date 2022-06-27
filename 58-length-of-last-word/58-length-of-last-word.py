class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        found = False
        l = len(s)
        i = l-1
        cnt = 0
        
        while i>=0:
            if not found:
                if s[i] != " ":
                    cnt += 1
                    found = True
            else:
                if s[i] == " ":
                    return cnt
                else:
                    cnt += 1
            i -= 1
        return cnt