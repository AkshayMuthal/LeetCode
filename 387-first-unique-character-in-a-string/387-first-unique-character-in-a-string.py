class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = [-1]*26
        ans = sys.maxsize
        for i in range(len(s)):
            val = ord(s[i])-97
            if char[val] == -1:
                char[val] = i
            else:
                char[val] = -2
        for i in char:
            if i>=0:
                ans = min(ans, i)
        return ans if ans != sys.maxsize else -1