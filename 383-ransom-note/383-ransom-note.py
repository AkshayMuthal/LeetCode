class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char = [0]*26
        for word in magazine:
            char[ord(word)-97] += 1
        
        for word in ransomNote:
            if char[ord(word)-97] <= 0:
                return False
            char[ord(word)-97] -= 1
        
        return True
        