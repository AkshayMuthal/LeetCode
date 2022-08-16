class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = [-1]*26
        ans = 100000
        for i in range(len(s)):
            val = ord(s[i])-97
            if char[val] == -1:
                char[val] = i
            else:
                char[val] = -2
        for i in range(26):
            if char[i]>=0:
                ans = min(ans, char[i])
        return ans if ans != 100000 else -1