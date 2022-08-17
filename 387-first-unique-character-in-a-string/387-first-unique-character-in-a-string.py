class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for i in range(len(s)):
            char[s[i]] = char.get(s[i], 0)+1
        for i in range(len(s)):
            if char[s[i]] == 1:
                return i
        return -1