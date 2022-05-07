class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = -10000000000
        stk = deque()
        for n in nums[::-1]:
            if n<s:
                return True
            while len(stk)>0 and n>stk[-1]:
                s = stk.pop()
            stk.append(n)
        return False