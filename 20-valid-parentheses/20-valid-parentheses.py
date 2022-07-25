class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        hm = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s:
            if c in hm:
                if stk and hm[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False