class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char = [0]*26
        for i in s:
            char[ord(i)-97] += 1
        
        l = 0
        for i in t:
            val = ord(i)-97
            if char[val] > 0:
                char[val] -= 1
                l += 1
        
        if l == len(s):
            return True
        return False