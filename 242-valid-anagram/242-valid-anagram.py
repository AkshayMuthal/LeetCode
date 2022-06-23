class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        char = [0]*26
        for i in s:
            char[ord(i)-97] += 1
        for i in t:
            char[ord(i)-97] -= 1
        for i in range(26):
            if char[i]!=0:
                return False
        return True