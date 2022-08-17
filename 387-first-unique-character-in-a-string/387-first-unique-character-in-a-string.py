class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = collections.Counter(s)
        for i,c in enumerate(s):
            if char[c] == 1:
                return i
        return -1