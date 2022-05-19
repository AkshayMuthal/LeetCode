class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = [-1 for i in range(256)]
        ans = 100001
        for i in range(len(s)):
            ind = ord(s[i])
            if char[ind] == -1:
                char[ind]=i
            else:
                char[ind] = -2
        for i in range(256):
            if char[i]>=0:
                ans = min(ans, char[i])
        return -1 if ans == 100001 else ans
            