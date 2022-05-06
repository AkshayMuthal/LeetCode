class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        stack.append([s[0], 1])
        same = 1
        prev = s[0]
        for i in range(1, len(s)):
            if prev == s[i]:
                same+=1
            else:
                same=1
            if same == k:
                for j in range(k-1):
                    stack.pop()
                if len(stack)>0:
                    elem = stack[-1]
                    prev = elem[0]
                    same = elem[1]
                else:
                    prev = ""
                    same = 0
            else:
                stack.append([s[i], same])
                prev = s[i]
        ans = ""
        while len(stack)>0:
            elem, freq = stack.pop()
            ans = elem + ans
        return ans
            