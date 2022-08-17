class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for c in s:
            char[c] = char.get(c, 0)+1
        for i,c in enumerate(s):
            if char[c] == 1:
                return i
        return -1