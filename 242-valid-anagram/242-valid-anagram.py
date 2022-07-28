class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char = [0]*26
        for i in s:
            char[ord(i)-97] += 1
        for i in t:
            char[ord(i)-97] -= 1
        for i in char:
            if i != 0:
                return False
        return True
        